# Heap & Priority Queue - Pattern

Questa cartella raccoglie problemi in cui serve estrarre ripetutamente il minimo, il massimo, il k-esimo elemento, oppure fondere piu' stream ordinati per priorita'.
In Python `heapq` implementa un **min heap**: l'elemento piu' piccolo sta in cima (`heap[0]`).

## Operazioni base

```python
import heapq

heap = []
heapq.heappush(heap, value)      # O(log n)
smallest = heapq.heappop(heap)   # O(log n)
top = heap[0]                    # O(1)

heapq.heapify(nums)              # O(n)
```

Per simulare un **max heap**, si inseriscono valori negati:

```python
heapq.heappush(heap, -value)
largest = -heapq.heappop(heap)
```

---

## Pattern 1: Max Heap con valori negati

**Quando usarlo**

Quando a ogni step serve prendere l'elemento piu' grande.

**Esercizi**

- `lastStoneWeight.py`: prende sempre le due pietre piu' pesanti.
- `findKthLargest.py`: una soluzione estrae il massimo `k` volte.
- `taskScheduler.py`: esegue sempre il task con frequenza residua maggiore.

**Idea**

Python ha solo min heap, quindi salvo `-x`. Il valore piu' grande diventa il piu' piccolo tra i negativi.

```python
max_heap = [-x for x in nums]
heapq.heapify(max_heap)

largest = -heapq.heappop(max_heap)
```

**Complessita tipica**

- Build heap: `O(n)`
- Ogni pop/push: `O(log n)`
- Spazio: `O(n)`

---

## Pattern 2: Min Heap di dimensione k

**Quando usarlo**

Quando serve mantenere i **k elementi piu' grandi** visti finora, oppure il k-esimo piu' grande in streaming.

**Esercizi**

- `KthLargest.py`: mantiene sempre i `k` valori piu' grandi nello stream.
- `findKthLargest.py`: soluzione ottimizzata con heap di dimensione `k`.

**Idea**

Il min heap contiene al massimo `k` elementi. La cima (`heap[0]`) e' il piu' piccolo tra i k piu' grandi, quindi e' il k-esimo piu' grande.

```python
min_heap = []

for num in nums:
    heapq.heappush(min_heap, num)
    if len(min_heap) > k:
        heapq.heappop(min_heap)

return min_heap[0]
```

**Perche' funziona**

Ogni volta che il heap supera `k`, elimino il valore piu' piccolo. Restano solo i candidati piu' grandi.

**Complessita tipica**

- Tempo: `O(n log k)`
- Spazio: `O(k)`

---

## Pattern 3: Max Heap di dimensione k

**Quando usarlo**

Quando serve mantenere i **k elementi piu' piccoli** visti finora.

**Esercizi**

- `KClosest.py`: soluzione con max heap per tenere solo i `k` punti piu' vicini all'origine.

**Idea**

Uso un max heap simulato con distanze negative. Se il heap supera `k`, rimuovo il punto piu' lontano tra quelli tenuti.

```python
max_heap = []

for x, y in points:
    dist = -(x * x + y * y)
    heapq.heappush(max_heap, (dist, x, y))
    if len(max_heap) > k:
        heapq.heappop(max_heap)

return [[x, y] for dist, x, y in max_heap]
```

**Nota**

Per confrontare distanze dall'origine non serve `sqrt`: `x^2 + y^2` mantiene lo stesso ordinamento.

**Complessita tipica**

- Tempo: `O(n log k)`
- Spazio: `O(k)`

---

## Pattern 4: Heap con tuple per priorita' multiple

**Quando usarlo**

Quando l'ordinamento dipende da piu' informazioni: priorita', id, indice, sorgente, timestamp.

**Esercizi**

- `KClosest.py`: tuple `(dist, x, y)`.
- `designTwitter.py`: tuple `(timestamp, tweetId, followeeId, index)`.

**Idea**

`heapq` confronta le tuple in ordine lessicografico: prima il primo campo, poi il secondo, ecc.

```python
heapq.heappush(heap, (priority, value, source_id, index))
priority, value, source_id, index = heapq.heappop(heap)
```

**Quando e' utile**

- recuperare il valore ordinato per priorita';
- sapere da quale lista/sorgente proviene;
- reinserire il prossimo elemento della stessa sorgente.

---

## Pattern 5: K-way merge / fusione di stream

**Quando usarlo**

Quando ci sono piu' liste o stream gia' ordinati per priorita' e serve produrre i migliori elementi globali.

**Esercizi**

- `designTwitter.py`: ogni followee ha una lista di tweet ordinata per tempo; il news feed prende i 10 tweet piu' recenti tra tutti.

**Idea**

Inserisco nel heap il tweet piu' recente di ogni followee. Ogni volta che ne estraggo uno, inserisco il tweet precedente dello stesso followee.

```python
heap = []

for user in followees:
    i = len(tweets[user]) - 1
    if i >= 0:
        time, tweet_id = tweets[user][i]
        heapq.heappush(heap, (time, tweet_id, user, i))

res = []
while heap and len(res) < 10:
    time, tweet_id, user, i = heapq.heappop(heap)
    res.append(tweet_id)

    if i > 0:
        next_time, next_tweet_id = tweets[user][i - 1]
        heapq.heappush(heap, (next_time, next_tweet_id, user, i - 1))
```

**Complessita tipica**

Se `f` e' il numero di followee e `m` il numero di elementi richiesti:

- Tempo: `O(f log f + m log f)`
- Spazio: `O(f)`

---

## Pattern 6: Due heap per la mediana

**Quando usarlo**

Quando arrivano numeri in streaming e bisogna trovare la mediana dopo ogni inserimento.

**Esercizi**

- `MedianFinder.py`

**Idea**

Mantengo due meta':

- `maxHeap`: meta' sinistra, con i numeri piu' piccoli, salvati negativi;
- `minHeap`: meta' destra, con i numeri piu' grandi.

Le dimensioni devono differire al massimo di 1.

```python
max_heap = []  # lower half, values negated
min_heap = []  # upper half

def add(num):
    heapq.heappush(max_heap, -num)
    heapq.heappush(min_heap, -heapq.heappop(max_heap))

    if len(min_heap) > len(max_heap) + 1:
        heapq.heappush(max_heap, -heapq.heappop(min_heap))

def median():
    if len(min_heap) == len(max_heap):
        return (min_heap[0] + (-max_heap[0])) / 2
    return min_heap[0]
```

**Invarianti**

- tutti gli elementi in `maxHeap` sono `<=` agli elementi in `minHeap`;
- le dimensioni sono bilanciate;
- la mediana si legge dalle cime.

**Complessita tipica**

- `addNum`: `O(log n)`
- `findMedian`: `O(1)`
- Spazio: `O(n)`

---

## Pattern 7: Heap + cooldown queue

**Quando usarlo**

Quando bisogna scegliere sempre l'elemento migliore disponibile, ma dopo l'uso deve aspettare un certo tempo prima di poter essere riutilizzato.

**Esercizi**

- `taskScheduler.py`

**Idea**

Uso:

- un max heap per i task disponibili, ordinati per frequenza residua;
- una queue per i task in cooldown, con il tempo in cui possono rientrare.

```python
from collections import deque

heap = [-freq for freq in counts.values()]
heapq.heapify(heap)
wait = deque()
time = 0

while heap or wait:
    time += 1

    if heap:
        freq = heapq.heappop(heap) + 1
        if freq < 0:
            wait.append((freq, time + n))

    if wait and wait[0][1] == time:
        freq, ready_time = wait.popleft()
        heapq.heappush(heap, freq)
```

**Complessita tipica**

- Tempo: `O(t log k)`, dove `t` e' il tempo simulato e `k` il numero di task diversi.
- Spazio: `O(k)`

---

## Pattern 8: Soluzione matematica/greedy quando il heap simula troppo

**Quando usarlo**

Quando il problema con heap funziona, ma esiste una formula o un ordinamento piu' diretto.

**Esercizi**

- `taskScheduler.py`: formula basata sul task piu' frequente.
- `lastStoneWeight.py`: bucket sort se i pesi sono limitati.
- `findKthLargest.py`: sorting come soluzione semplice.
- `KClosest.py`: quickselect come alternativa media `O(n)`.

**Esempio: Task Scheduler**

```python
maxf = max(count)
max_count = count.count(maxf)
time = (maxf - 1) * (n + 1) + max_count
return max(len(tasks), time)
```

**Regola pratica**

Il heap e' spesso la soluzione piu' intuitiva e generale. Pero', se:

- il dominio dei valori e' piccolo, valuta bucket/counting sort;
- serve solo il k-esimo elemento, valuta quickselect;
- il problema ha una struttura a blocchi/frequenze, cerca una formula greedy.

---

## Come riconoscere il pattern giusto

| Problema | Pattern |
| --- | --- |
| Devo prendere sempre il massimo | Max heap con valori negati |
| Devo prendere sempre il minimo | Min heap standard |
| Devo trovare il k-esimo piu' grande | Min heap di dimensione k |
| Devo trovare i k elementi piu' piccoli | Max heap di dimensione k |
| Devo fondere elementi ordinati da piu' liste | Heap con tuple + k-way merge |
| Devo gestire una mediana dinamica | Due heap bilanciati |
| Devo rispettare cooldown/attese | Heap + queue |
| I valori sono limitati o c'e' una formula | Bucket / greedy / math |

---

## Checklist mentale

1. Quale elemento devo estrarre spesso: minimo, massimo, k-esimo?
2. Il heap deve contenere tutti gli elementi o solo `k`?
3. Mi serve mantenere informazioni extra nella tupla?
4. Gli elementi estratti devono essere reinseriti modificati?
5. Ci sono cooldown, stream, timestamp o piu' sorgenti?
6. Esiste una soluzione piu' diretta con sorting, bucket, greedy o math?
