def popular_words(st, lst):
   st = st.lower().split()
   x = {}
   for i in lst:
       x[i] = st.count(i)
   return x

print(popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']))