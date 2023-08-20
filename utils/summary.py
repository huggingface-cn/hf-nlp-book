import re
import pandas as pd
mdx_file='Course/publish/all/all.mdx'
res=re.findall('```.*?```',open(mdx_file,'r',encoding='utf-8').read(),re.S)
res=[[i.count('\n'),i] for i in res ]
res.sort(key=lambda x:x[0],reverse=True)
df=pd.DataFrame(res,columns=['length','code'])
df.to_excel('code.xlsx',index=False)