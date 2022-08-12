import os
import sys


company=sys.argv[1]
token = str(os.environ.get('github_token'))
amass=os.environ.get('a_mass')
v1l03t = os.environ.get('v_1l03t')

sub = 'python ~/tools/github-search/github-subdomains.py -t '+token +'  -d ~/recon/gh0str3c0n/'+company +'/scope.txt > ~/recon/gh0str3c0n/' + company + '/gout.txt '
findo = 'findomain -f ~/recon/gh0str3c0n/'+company + '/scope.txt -o  ~/recon/gh0str3c0n/'+company + '/findo.txt'
vi = 'bash ~/tools/Gh0stR3con/back-end/v1l03t/v1l03t ~/recon/gh0str3c0n/' + \
    company + '/scope.txt '+company
sub1 = 'subfinder -dL ~/recon/gh0str3c0n/'+company + '/scope.txt -o ~/recon/gh0str3c0n/'+company + '/sout.txt '
sub2 = 'amass enum -passive -df ~/recon/gh0str3c0n/'+company +'/scope.txt -o ~/recon/gh0str3c0n/'+company + '/aout.txt'
sort = 'cat ~/recon/gh0str3c0n/'+company + '/*.txt | sort -u >> ~/recon/gh0str3c0n/'+company + '/all.txt'
naabu = 'naabu -list ~/recon/gh0str3c0n/'+company + '/all.txt -o ~/recon/gh0str3c0n/'+company + '/nabu.txt'
liv = ' cat ~/recon/gh0str3c0n/'+company + '/nabu.txt |  httpx | tee -a ~/recon/gh0str3c0n/'+company + '/live.txt'
m4skup='bash m4skup/m4skup '+company
gau = 'cat ~/recon/gh0str3c0n/'+company+'/live.txt | gau --o ~/recon/gh0str3c0n/'+company+'/gau.txt'
wayback = 'cat ~/recon/gh0str3c0n/'+company+'/live.txt | waybackurls > ~/recon/gh0str3c0n/'+company+'/waybackurls.txt'
dirsearch = ' python3 ~/tools/dirsearch/dirsearch.py -l ~/recon/gh0str3c0n/'+company+'/live.txt -e php,asp,aspx,net,js,cs,php2,php3,php4,php5,php6,php7,jsp,java,python,yaml,yml,config,conf,htaccess,htpasswd,shtml -o  ~/recon/gh0str3c0n/'+company+'/dirse.txt'
paramspi = 'cat ~/recon/gh0str3c0n/'+company + '/all.txt| xargs -n1 -P4  python3 ~/tools/ParamSpider/paramspider.py -d >>  ~/recon/gh0str3c0n/' + company+'/paramspider.txt'
gfxss = 'cat ~/recon/gh0str3c0n/'+company + '/paramspider.txt| gf xss >  ~/recon/gh0str3c0n/'+company+'/xss.txt'
gfsqli = 'cat ~/recon/gh0str3c0n/'+company + '/paramspider.txt| gf sqli >  ~/recon/gh0str3c0n/'+company+'/sqli.txt'
gfssrf = 'cat ~/recon/gh0str3c0n/'+company + '/paramspider.txt| gf ssrf >  ~/recon/gh0str3c0n/'+company+'/ssrf.txt'
gfssti = 'cat ~/recon/gh0str3c0n/'+company + '/paramspider.txt| gf ssti >  ~/recon/gh0str3c0n/'+company+'/ssti.txt'
gfidor = 'cat ~/recon/gh0str3c0n/'+company + '/paramspider.txt| gf idor >  ~/recon/gh0str3c0n/'+company+'/idor.txt'
gflfi = 'cat ~/recon/gh0str3c0n/'+company + '/paramspider.txt| gf lfi >  ~/recon/gh0str3c0n/'+company+'/lfi.txt'
gfrce = 'cat ~/recon/gh0str3c0n/'+company + '/paramspider.txt| gf rce >  ~/recon/gh0str3c0n/'+company+'/rce.txt'
gfredr = 'cat ~/recon/gh0str3c0n/'+company + '/paramspider.txt| gf redirect >  ~/recon/gh0str3c0n/'+company+'/redirect.txt'


if (amass=="true"):
    print("amass")
    os.system(sub2)
if (v1l03t=="true"):
    os.system(vi)

os.system(sub)
os.system(findo)
os.system(sub1)
os.system(sort)
os.system(naabu)
os.system(liv)
os.system(m4skup)
os.system(gau)
os.system(wayback)
os.system(dirsearch)
os.system(paramspi)
os.system(gfxss)
os.system(gfsqli)
os.system(gfssrf)
os.system(gfssti)
os.system(gfidor)
os.system(gflfi)
os.system(gfrce)
os.system(gfredr)
