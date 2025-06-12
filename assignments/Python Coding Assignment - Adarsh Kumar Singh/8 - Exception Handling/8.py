try:
   open("nofile.txt")
except OSError as e:
   raise RuntimeError("unable to handle error") from e