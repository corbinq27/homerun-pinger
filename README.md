# homerun-pinger
Send an IFTTT alert when my homerun device goes offline

In IFTTT, set up a "maker" applet and get the key from https://ifttt.com/maker_webhooks and click on "documentation".

Add your key to the "IFTTT_KEY" string.
Change your HOMERUN_URL to the URL you're expecting to give you a 200 when you do the get request on that URL.

Use crontab to run this python script at a cadence of your choosing (crontab.guru is a great website to help you figure out a cadence.)

EVENT can be changed to whatever you want. When you create an IFTTT maker applet, be sure you have a matching event name.
