filename = 'pricelog' + '.txt'
f = open(filename,"w+")
# while (True):
  # print("exit(), control + C")
  # for i in range(10):
f.write("This is line {k}\r\n".format(k=6))
f.write("This is line %d\r\n" % (4))
f.close()