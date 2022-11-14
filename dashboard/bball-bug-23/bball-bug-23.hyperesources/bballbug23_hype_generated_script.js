//	HYPE.documents["bball-bug-23"]

(function(){(function m(){function k(a,b,c,d){var e=!1;null==window[a]&&(null==window[b]?(window[b]=[],window[b].push(m),a=document.getElementsByTagName("head")[0],b=document.createElement("script"),e=l,false==!0&&(e=""),b.type="text/javascript",""!=d&&(b.integrity=d,b.setAttribute("crossorigin","anonymous")),b.src=e+"/"+c,a.appendChild(b)):window[b].push(m),e=!0);return e}var l="bball-bug-23.hyperesources",f="bball-bug-23",g="bballbug23_hype_container";if(false==
!1)try{for(var c=document.getElementsByTagName("script"),a=0;a<c.length;a++){var d=c[a].src,b=null!=d?d.indexOf("/bballbug23_hype_generated_script.js"):-1;if(-1!=b){l=d.substr(0,b);break}}}catch(p){}c=navigator.userAgent.match(/MSIE (\d+\.\d+)/);c=parseFloat(c&&c[1])||null;d=!0==(null!=window.HYPE_736F||null!=window.HYPE_dtl_736F)||false==!0||null!=c&&10>c;a=!0==d?"HYPE-736.full.min.js":"HYPE-736.thin.min.js";c=!0==d?"F":"T";d=d?"":
"";if(false==!1&&(a=k("HYPE_736"+c,"HYPE_dtl_736"+c,a,d),false==!0&&(a=a||k("HYPE_w_736","HYPE_wdtl_736","HYPE-736.waypoints.min.js","")),false==!0&&(a=a||k("Matter","HYPE_pdtl_736","HYPE-736.physics.min.js","")),a))return;d=window.HYPE.documents;if(null!=d[f]){b=1;a=f;do f=""+a+"-"+b++;while(null!=d[f]);for(var e=document.getElementsByTagName("div"),
b=!1,a=0;a<e.length;a++)if(e[a].id==g&&null==e[a].getAttribute("HYP_dn")){var b=1,h=g;do g=""+h+"-"+b++;while(null!=document.getElementById(g));e[a].id=g;b=!0;break}if(!1==b)return}b=[];b=[{name:"initFunctions",source:"function(hypeDocument, element, event) {\twindow.changeLogo = function (team, url) {\n\t\t// team - 'home' or 'visitor'\n\t\t// url - image src\n\t\tlet key = `${team}Logo`\n\t\tlet element = hypeDocument.getElementById(key)\n\t\thypeDocument.setElementProperty(element, 'background-image', url)\n\t}\n\t\n\twindow.changeText = function (key, value) {\n\t\thypeDocument.getElementById(key).innerText = value\n\t}\n\t\n\twindow.incHomeScore = function() {\n\t\thypeDocument.continueTimelineNamed('Home Score Change', hypeDocument.kDirectionForward)\n\t}\n}",identifier:"43"},{name:"incHomeScoreAnimator",source:"function(hypeDocument, element, event) {\tlet ele = hypeDocument.getElementById('homeScoreAnimator')\n\tele.innerText = window.store['homeScore']\n}",identifier:"49"},{name:"incHomeScore",source:"function(hypeDocument, element, event) {\tlet ele = hypeDocument.getElementById('homeScore')\n\tele.innerText = window.store['homeScore']\n}",identifier:"79"},{name:"initSocket",source:"function(hypeDocument, element, event) {\tconst sock = io(\"localhost:8080\")\n\twindow.store = {}\n\t\n\tlet overrides = {\n\t\t\"homeScore\": () => {\n\t\t\thypeDocument.continueTimelineNamed('Home Score Change', hypeDocument.kDirectionForward, false)\n\t\t}\n\t}\n\t\n\tfunction update(payload) {\n\t\tlet oldStore = {...window.store}\n\t\twindow.store = {...window.store, ...payload}\n\t\tconsole.log(oldStore, payload)\n\t\tObject.keys(payload).forEach((key) => {\n\t\t\tlet isChanged = oldStore[key] != payload[key]\n\t\t\tconsole.log(key, payload[key], isChanged)\n\t\t\tif(key in overrides && isChanged) {\n\t\t\t\toverrides[key]()\n\t\t\t} else {\n\t\t\t\ttry {\n\t\t\t\t\thypeDocument.getElementById(key).innerText = payload[key]\n\t\t\t\t} catch (_) {}\n\t\t\t}\n\t\t})\n\t}\n\t\n\tsock.on(\"store_init\", update)\n\tsock.on(\"store_patch\", update)\n}",identifier:"84"}];e={};h={};for(a=0;a<b.length;a++)try{h[b[a].identifier]=b[a].name,e[b[a].name]=eval("(function(){return "+b[a].source+"})();")}catch(n){window.console&&window.console.log(n),e[b[a].name]=function(){}}c=new window["HYPE_736"+c](f,g,{"3":{p:1,n:"OLD_DOMINION.png",g:"39",t:"@1x"},"1":{p:1,n:"Screenshot.png",g:"20",o:true,t:"@1x"},"-2":{n:"blank.gif"},"-1":{n:"PIE.htc"},"2":{p:1,n:"DREXEL.png",g:"38",t:"@1x"},"0":{p:1,n:"DrexelDragonsAlt.png",g:"18",o:true,t:"@1x"}},l,["<link href='https://fonts.googleapis.com/css?family=Barlow:700&subset=latin' rel='stylesheet' type='text/css'>","<link href='https://fonts.googleapis.com/css?family=Barlow:800&subset=latin' rel='stylesheet' type='text/css'>","<link href='https://fonts.googleapis.com/css?family=Barlow:700italic&subset=latin' rel='stylesheet' type='text/css'>"],e,[{n:"Untitled Scene",o:"1",X:[0]}],
[{A:{a:[{p:4,h:"43"},{p:4,h:"84"}]},o:"3",dA:{a:[{p:0}]},p:"600px",cA:false,Y:1920,Z:1080,c:"#FFF",L:[],bY:1,d:1920,U:{},T:{"48":{q:false,z:0.12,i:"48",n:"Home Score Change",a:[{f:"c",y:0,z:0.12,i:"b",e:-10,s:47,o:"106"},{f:"c",y:0,z:0.12,i:"b",e:-70,s:-10,o:"107"},{f:"c",p:2,y:0,z:0.12,i:"ActionHandler",e:{a:[{p:4,h:"79"},{i:0,b:"48",p:9,symbolOid:"2"}]},s:{a:[{p:4,h:"49"},{p:7,b:"48",symbolOid:"2"}]},o:"48"},{y:0.12,i:"b",s:-10,z:0,o:"106",f:"c"},{y:0.12,i:"b",s:-70,z:0,o:"107",f:"c"},{f:"c",p:2,y:0.12,z:0,i:"ActionHandler",s:{a:[{p:4,h:"79"},{i:0,b:"48",p:9,symbolOid:"2"}]},o:"48"}],f:30,b:[]},kTimelineDefaultIdentifier:{q:false,z:0,i:"kTimelineDefaultIdentifier",n:"Main Timeline",a:[],f:30,b:[]}},bZ:180,O:["88","102","108","93","107","92","97","87","96","100","104","101","109","105","85","98","103","91","86","90","95","94","89","106","99"],n:"Untitled Layout","_":0,v:{"92":{aU:8,bB:0,G:"#000",c:242,aV:8,r:"inline",d:62,bC:2,s:"Barlow",t:52,u:"normal",Z:"break-word",v:"800",i:"clock",w:"10:00<br>",j:"absolute",x:"visible",aZ:5,k:"div",y:"preserve",z:9,aS:8,aT:8,a:828,bA:"#000",F:"center",b:952},"103":{c:147,d:67,I:"Solid",J:"Solid",K:"Solid",g:"#131313",L:"Solid",M:0,N:0,A:"#D8DDE4",x:"visible",j:"absolute",B:"#D8DDE4",P:0,k:"div",C:"#D8DDE4",z:11,O:0,D:"#D8DDE4",a:1740,b:962},"85":{c:103,d:65,I:"None",J:"None",K:"None",g:"#023562",L:"None",M:0,i:"homeScoreBox",N:0,A:"#D8DDE4",x:"visible",j:"absolute",B:"#D8DDE4",P:0,O:0,C:"#D8DDE4",z:5,k:"div",D:"#D8DDE4",a:725,b:963},"93":{aU:8,G:"#FFF",c:87,aV:8,r:"inline",d:70,s:"Barlow",t:58,Z:"break-word",v:"700",i:"visitorScore",w:"10",j:"absolute",x:"visible",k:"div",y:"preserve",z:18,aS:8,aT:8,a:322,F:"center",b:953},"86":{aU:8,G:"#FFF",aV:8,r:"inline",s:"Barlow",t:39,u:"italic",Z:"break-word",v:"700",i:"homeTeamName",w:"DREXEL<br>",j:"absolute",x:"visible",yy:"nowrap",k:"div",y:"preserve",z:17,aS:8,aT:8,a:436,b:965},"108":{b:883,z:23,K:"Solid",c:90,L:"Solid",d:15,aS:6,M:1,bD:"none",N:1,aT:6,dB:"button",O:1,g:"#F0F0F0",aU:6,P:1,aV:6,j:"absolute",k:"div",aI:4,aJ:4,aK:4,aL:4,A:"#A0A0A0",B:"#A0A0A0",Z:"break-word",r:"none",C:"#A0A0A0",D:"#A0A0A0",t:13,aA:{a:[{b:"48",p:8,z:false,symbolOid:"2",J:false}]},F:"center",G:"#000",aP:"pointer",w:"+2<br>",x:"visible",I:"Solid",a:537,y:"preserve",J:"Solid"},"104":{c:103,d:65,I:"None",J:"None",K:"None",g:"#031D34",L:"None",M:0,i:"visitorScoreBox",N:0,A:"#D8DDE4",x:"visible",j:"absolute",B:"#D8DDE4",P:0,O:0,C:"#D8DDE4",z:4,k:"div",D:"#D8DDE4",a:322,b:963},"87":{x:"hidden",k:"div",c:285,d:65,z:14,e:0.35,a:21,j:"absolute",b:963},"94":{h:"20",p:"no-repeat",x:"visible",a:1246,dB:"img",q:"100% 100%",j:"absolute",r:"inline",z:13,k:"div",b:973,d:46,c:352},"109":{c:393,d:65,I:"None",J:"None",K:"None",g:"#00437B",L:"None",M:0,i:"homeBox",N:0,A:"#D8DDE4",x:"visible",j:"absolute",B:"#D8DDE4",P:0,O:0,C:"#D8DDE4",z:3,k:"div",D:"#D8DDE4",a:435,b:963},"100":{c:393,cP:".visitorBox",d:65,I:"None",J:"None",K:"None",g:"#00325B",L:"None",M:0,i:"visitorBox",N:0,A:"#D8DDE4",x:"visible",j:"absolute",B:"#D8DDE4",P:0,O:0,C:"#D8DDE4",z:2,k:"div",D:"#D8DDE4",a:32,b:963},"95":{aU:8,bB:0,G:"#000",aV:8,r:"inline",bC:2,s:"Barlow",t:30,Z:"break-word",v:"700",i:"shotClock",w:":30<br>",j:"absolute",x:"visible",yy:"nowrap",aZ:5,y:"preserve",k:"div",z:8,aS:8,aT:8,a:1024,bA:"#000",F:"center",b:969},"88":{h:"39",p:"no-repeat",x:"visible",a:-68,dY:[],q:"100% 100%",j:"absolute",r:"inline",z:1,bF:"87",b:-116,d:285,dB:"img",i:"visitorLogo",k:"div",c:422},"105":{k:"div",x:"hidden",c:103,d:65,z:19,a:725,j:"absolute",b:963},"96":{c:1855,d:5,I:"Solid",J:"Solid",K:"Solid",g:"#948F8F",L:"Solid",M:0,N:0,A:"#D8DDE4",x:"visible",j:"absolute",B:"#D8DDE4",P:0,k:"div",C:"#D8DDE4",z:21,O:0,D:"#D8DDE4",a:32,b:956},"89":{h:"18",p:"no-repeat",x:"visible",a:1758,dB:"img",q:"100% 100%",j:"absolute",r:"inline",z:12,k:"div",b:965,d:62,c:111},"101":{x:"hidden",k:"div",c:285,d:65,z:15,e:0.35,a:435,j:"absolute",b:963},"97":{c:1918,d:69,I:"None",J:"None",K:"None",g:"#DFDFDF",L:"None",M:0,N:0,A:"#D8DDE4",x:"visible",j:"absolute",B:"#D8DDE4",P:0,k:"div",C:"#D8DDE4",z:1,O:0,D:"#D8DDE4",a:1,b:961},"106":{aU:8,G:"#FFF",c:87,aV:8,r:"inline",d:70,s:"Barlow",t:58,Z:"break-word",v:"700",i:"homeScoreAnimator",w:"10",bF:"105",j:"absolute",x:"visible",k:"div",y:"preserve",z:2,aS:8,aT:8,a:0,F:"center",b:47},"98":{c:654,d:67,I:"Solid",J:"Solid",K:"Solid",g:"#292828",L:"Solid",M:0,N:0,A:"#D8DDE4",x:"visible",j:"absolute",B:"#D8DDE4",P:0,k:"div",C:"#D8DDE4",z:10,O:0,D:"#D8DDE4",a:1086,b:962},"90":{aU:8,bB:0,G:"#000",aV:8,r:"inline",bC:2,s:"Barlow",t:30,Z:"break-word",v:"700",i:"period",w:"2nd<br>",j:"absolute",x:"visible",yy:"nowrap",aZ:5,y:"preserve",k:"div",z:7,aS:8,aT:8,a:828,bA:"#000",F:"center",b:970},"102":{h:"38",p:"no-repeat",x:"visible",a:-94,dY:[],q:"100% 100%",j:"absolute",r:"inline",z:1,bF:"101",b:-110,d:285,dB:"img",i:"homeLogo",k:"div",c:422},"99":{c:1855,d:5,I:"Solid",J:"Solid",K:"Solid",g:"#948F8F",L:"Solid",M:0,N:0,A:"#D8DDE4",x:"visible",j:"absolute",B:"#D8DDE4",P:0,k:"div",C:"#D8DDE4",z:22,O:0,D:"#D8DDE4",a:32,b:1030},"91":{aU:8,G:"#FFF",aV:8,r:"inline",s:"Barlow",t:39,u:"italic",Z:"break-word",v:"700",i:"visitorTeamName",w:"OLD DOMINION<br>",j:"absolute",x:"visible",yy:"nowrap",k:"div",y:"preserve",z:16,aS:8,aT:8,a:33,b:965},"107":{aU:8,G:"#FFF",c:87,aV:8,r:"inline",d:70,s:"Barlow",t:58,Z:"break-word",v:"700",i:"homeScore",w:"10",bF:"105",j:"absolute",x:"visible",k:"div",y:"preserve",z:1,aS:8,aT:8,a:0,F:"center",b:-10}}}],{},h,{},null,false,false,-1,true,true,false,true,true);d[f]=c.API;document.getElementById(g).setAttribute("HYP_dn",f);c.z_o(this.body)})();})();
