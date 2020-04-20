# test-task
Дано:

Cкрипт на любом языке программирования, который бы вывел top-10 ip, на которые было отдано больше всего трафика ($body_bytes_sent в логе). Сортировать нужно по убыванию трафика.

Небольшой коммент:
1. top10_body_bytes_sent.py - реализован вывод топ-10 ip по максимальному трафику на 1 запрос, сортировка трафика по убыванию

2. top10_body_bytes_sent_summary.py - реализован вывод топ-10 ip по максимальному трафику по всем запросам, сортировка трафика по убыванию:

./top10_body_bytes_sent_summary.py ../test.log

Top-10 ip with high traffic, sorted by summary traffic:

ip address: 195.77.230.187 traffic: 286634 bytes
ip address: 195.77.230.189 traffic: 190753 bytes
ip address: 195.77.230.23 traffic: 51997 bytes
ip address: 195.77.230.185 traffic: 51261 bytes
ip address: 195.77.230.24 traffic: 44825 bytes
ip address: 195.77.230.186 traffic: 43032 bytes
ip address: 195.77.230.166 traffic: 37653 bytes
ip address: 195.77.230.176 traffic: 37233 bytes
ip address: 195.77.230.196 traffic: 35860 bytes
ip address: 195.77.230.21 traffic: 34067 bytes

Only ip addresses:

195.77.230.187
195.77.230.189
195.77.230.23
195.77.230.185
195.77.230.24
195.77.230.186
195.77.230.166
195.77.230.176
195.77.230.196
195.77.230.21