def count_up_to(n):
  count = 1
  while count <= n:
    count += 1
    yield count

for num in count_up_to(5):
  print(num)
