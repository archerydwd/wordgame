# wordgame
python wordgame on OVH vps tutorial

=
###Set up git repo

I created a new git repo on github.com and followed the provided instructions to initialise my wordgame application folder as a git repo.

=
###Set up OVH vps

Go to https://www.ovh.ie/vps/vps-classic.xml and order the VPS Classic 1 for €2.

* Under the My VPS heading you can leave the settings as they are.
* Under the My Location heading select Europe Roubaix which is the closest location to Ireland.
* Under the My OS heading change the distribution to Ubuntu and the version to Ubuntu 14.10 Server 64bits and the language to English.

Continue with the order. Once done you will be provided with a link to the page to view your server and an ip address.

=
###Get Wordgame on the server

issue the following command, replacing my ip address with yours:

```
ssh root@46.105.16.62
```

change directory to var/www/

Then issue the following command:

```
git clone https://github.com/archerydwd/wordgame.git
```




