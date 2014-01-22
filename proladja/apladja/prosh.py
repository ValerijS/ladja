
import yaml
import csv
#fowr = input("Please enter: 'models.py'>__>")
yash = input("Please enter 'name' for yaml.py file:")
#with open(fowr, 'w') as cf:
# swr = csv.writer(cf, delimiter=' ')
 #swr.writerow(['from', 'django.db','import','models'])
st=file(yash, 'r')
d=yaml.load(st)
for nt in iter(d):
 sha=['class',nt+'(models.Model):'] 
 d1=d[nt]
 with open('admin.py', 'a') as cf:
    swr = csv.writer(cf, delimiter=' ')
    swr.writerow(['from','apladja.models','import',nt])
    swr.writerow(['admin.site.register('+nt+')'])
 with open('models.py', 'a') as cf:
    swr = csv.writer(cf, delimiter=' ')
    swr.writerow( sha) 
 i=0 
 while i < len(d1['fields']):
  l=d1['fields']
  nf=l[i]['id']
  if l[i]['type'] in 'char':
    ty1='models.CharField(max_length=128,' 
    ty2='unique=True)'
    with open('models.py', 'a') as cf:
      swr = csv.writer(cf, delimiter=' ')
      swr.writerow( [None,nf+'='+ty1+ty2])
  elif l[i]['type'] in 'int':
     ty='models.IntegerField(default=0)'
     with open('models.py', 'a') as cf:
      swr = csv.writer(cf, delimiter=' ')
      swr.writerow( [None,nf+'='+ty])
  elif l[i]['type'] in 'date':
     ty='models.DateField()'         
     with open('models.py', 'a') as cf:
      swr = csv.writer(cf, delimiter=' ')
      swr.writerow( [None,nf+'='+ty])
  else:
     ty='invalid type'  
     with open(fowr, 'a') as cf:
      swr = csv.writer(cf, delimiter=' ')
      swr.writerow( [None,nf+'='+ty])
  i=i+1
