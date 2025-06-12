import re
query = "name=adarsh&age=24&city=indore"
pattern = r'([^=&]+)=([^&]*)'
matches = re.findall(pattern, query)
query_dict = dict(matches)
print("Parsed Query:", query_dict)

