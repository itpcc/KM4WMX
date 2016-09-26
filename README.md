# KM4WMX
## Additional script run in multiple console (using "screen" each of command)

all script placed in `/home/echolink_proxy/` (Except noip which descripted in [NO-IP document](http://www.noip.com/support/knowledgebase/installing-the-linux-dynamic-update-client/))
```bash
java -jar /home/echolink_proxy/EchoLinkProxy.jar
/home/echolink_proxy/websocketd --port=8080 --devconsole python /home/echolink_proxy/read_callsign.py #Websocket
sudo /usr/local/bin/noip2
```

## Preinstall in proxy server
- screen
- java
- [Echolink Proxy server](http://www.echolink.org/register_data.jsp) in `/home/echolink_proxy/`
- [Websocketd](https://github.com/joewalnes/websocketd) in `/home/echolink_proxy/`