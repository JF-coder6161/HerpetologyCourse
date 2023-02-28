

import re

# .*?

text = '<12> <xyz> <!@#$%> <>'

ret = re.findall("<.+?>",text) # ['<12>', '<xyz>', '<!@#$%>']
print(ret)
ret = re.findall("<.*?>",text) # ['<12>', '<xyz>', '<!@#$%>', '<>']
print(ret)

# 案例2
# 模式修正符
# 修正符

