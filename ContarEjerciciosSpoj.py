import requests
import time

url_base = 'https://www.spoj.com/users/'
usuarios = ["kosaksi", "itactuk"]

def extraer_nombres_ejercicios(contenido_perfil):
    """
    Esta función debe de extraer los nombres de los ejercicios de un texto similar
    al del contenido de la variable ejemplo_contenido_perfil.
    Debe de devolver un listado con los nombres de los ejercicios.
    Si contenido_perfil es igual a ejemplo_contenido_perfil, entonces debe de
    retornar la lista ['ABSYS','ARITH2','CANTON','FCTRL2','INVCNT','NY10A','PT07Z','ACODE','ARMY','COINS','FENCE1','JULKA','OFFSIDE','SAMER08F','ACPC10A','ARRAYSUB','CRDS','GIRLSNBS','LASTDIG','OLOLO','SBANK','ADDREV','BEENUMS','EASYPROB','GSS1','LASTDIG2','ONP','STAMPS','AE00','BISHOPS','EDIST','GSS3','MARBLES','PALIN','STPAR','AGGRCOW','BITMAP','EIGHTS','HANGOVER','MAXLN','PARTY','TEST','AIBOHP','BUGLIFE','ETF','HORRIBLE','MIXTURES','PERMUT2','TOANDFRO','AMR10G','BYTESM2','FARIDA','HOTELS','NGM','PIGBANK','TRICOUNT','ANARC09A','CANDY','FASHION','HPYNOS','NHAY','PRIME1','TRT','AP2','CANDY3','FCTRL','HUBULLU','NSTEPS','PT07Y','WILLITST']
    """
    pass

def contar_ejercicios_spoj():
    resultado = {}
    for u in usuarios:
        contenido = requests.get(url_base+u+"/").content.decode('ISO-8859-1')
        ejercicios = extraer_nombres_ejercicios(contenido)
        for e in ejercicios:
            if e not in resultado:
                resultado[e] = {'cantidad':1,'usuarios':[u]}
            else:
                resultado[e]['cantidad']+=1
                resultado[e]['usuarios'].append(u)
        time.sleep(1.5)
    return resultado

def imprimir_conteo_ejercicios():
    detalle_ejercicios = contar_ejercicios_spoj()
    for ej, det in detalle_ejercicios.items():
        nombre_ejercicio = ej
        cantidad = det['cantidad']
        lista_usuarios = det['usuarios']
        print(nombre_ejercicio,cantidad,lista_usuarios)

imprimir_conteo_ejercicios()

ejemplo_contenido_perfil="""
<!DOCTYPE html>
<!--[if lt IE 7 ]><html class="ie ie6" lang="en"> <![endif]-->
<!--[if IE 7 ]><html class="ie ie7" lang="en"> <![endif]-->
<!--[if IE 8 ]><html class="ie ie8" lang="en"> <![endif]-->
<!--[if (gte IE 9)|!(IE)]><!--><html class="not-ie" lang="en"> <!--<![endif]-->
<head>
	<!-- main header -->
	<meta charset="utf-8">
	
				<title>Sphere Online Judge (SPOJ)  - User kosaksi</title>
	  
	<meta name="keywords" content="language, algorithm, spoj, contest, contester, Java, C#, Pascal, C, C++, python, ruby, caml, ocaml, perl, haskell, lisp, prolog, fortran, assembler, asembler, functional, online, judge, problem, problemset, ACM">
  	<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  
  		<meta property="og:image" content="//stx1.spoj.com/gfx/spoj-fb.jpg"/>
	<meta property="og:description" content="SPOJ (Sphere Online Judge) is an online judge system with over 315,000 registered users and over 20000 problems. The solution to problems can be submitted in over 60 languages including C, C++, Java, Python, C#, Go, Haskell, Ocaml, and F#. SPOJ has a rapidly growing problem set/tasks available for practice 24 hours/day, including many original tasks prepared by the community of expert problem setters associated with the project."/>
	<meta name="description" content="SPOJ (Sphere Online Judge) is an online judge system with over 315,000 registered users and over 20000 problems. The solution to problems can be submitted in over 60 languages including C, C++, Java, Python, C#, Go, Haskell, Ocaml, and F#. SPOJ has a rapidly growing problem set/tasks available for practice 24 hours/day, including many original tasks prepared by the community of expert problem setters associated with the project."/>
		<meta property="og:site_name" content="spoj.com"/>

  <!--[if (gte IE 9)|!(IE)]>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" id="metatag">
  <![endif]--> 

	  <!-- Favicon -->
	  <link href="//stx1.spoj.com/gfx/favicon_new.png" rel="shortcut icon" type="image/x-icon" />
	  
	  <!-- RSS -->
	  <link href="/rss/" rel="alternate" type="application/rss+xml" title="RSS Feed">
	
	  <!-- Web Fonts -->
	  <link href="https://fonts.googleapis.com/css?family=Open+Sans:300,400,600,700,800" rel="stylesheet" type="text/css">  

	<!-- Internet Explorer condition - HTML5 shim, for IE6-8 support of HTML5 elements -->
	<!--[if lt IE 9]>
		<script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>
	<![endif]--> 
	
	
	
	<!-- CSS: Bootstrap, Font-awesome, Bootstrap libs,  -->
	<link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css" rel="stylesheet" />
  	<link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css" rel="stylesheet">
  	<link href="//stx1.spoj.com/gfx/bootstrap-tour/build/css/bootstrap-tour.min.css" rel="stylesheet" />
  	<link href="//stx1.spoj.com/themes/bootstrap-social.css" rel="stylesheet" type="text/css" />
  	
	<link href="//stx1.spoj.com/themes/common.css?7" rel="stylesheet" type="text/css" id="theme0" />
	<link href="//stx1.spoj.com/themes/en_new.css?7" rel="stylesheet" type="text/css" id="theme" />
	
	<!-- JS -->
	<script type="text/javascript" src='//code.jquery.com/jquery-1.11.1.min.js'></script>
	<script type="text/javascript" src="//code.jquery.com/ui/1.11.2/jquery-ui.min.js"></script>
	
		<link href="//stx1.spoj.com/themes/cal-heatmap.css" rel="stylesheet" type="text/css">
	<script type="text/javascript" src='//stx1.spoj.com/js/d3.v3.min.js'></script>
	<script type="text/javascript" src='//stx1.spoj.com/js/cal-heatmap.min.js'></script>
	<script type="text/javascript" src="//www.google.com/jsapi"></script>
		
	<script type="text/javascript" src="https://maps.googleapis.com/maps/api/js?sensor=false"></script>	
	<script type="text/javascript" language="javascript">
	$(function () { 
		$("#profile-menu").popover();
	});
	function UnCryptMailto(s) {
		var n=0;
		var r="";
		for(var i=0;i<s.length;i++) {		
			n=s.charCodeAt(i); 
			if (n>=8364) {n = 128;}
			r += String.fromCharCode(n+(2));	
		}
		return r;
	}
	function linkTo_UnCryptMailto(s)	{
		location.href=UnCryptMailto(s);
	}
	</script>
	
	<script type="text/javascript">
	function recordOutboundLink(link, category, action) {
	  try {
	    var pageTracker=_gat._getTracker("UA-XXXXX-X");
	    pageTracker._trackEvent(category, action);
	    setTimeout('document.location = "' + link.href + '"', 100)
	  }catch(err){}
	}
	</script>
	
</head>

<body>

	
	<!-- <div class="space30"></div> -->
	
	<!-- Content -->
	<div class="content">
		<div class="container" id="header">
			<div class="row">
				<div class="col-md-12 text-right">
					
										
					
				</div>
			</div>
		
			<div class="row">
				<div class="col-md-4">
					<a href="/" class="navbar-brand">
						<img src="//stx1.spoj.com/gfx/2015e.png" style="height: 40px;"/>
					</a>
					<div class="navbar-header">
				      <button class="navbar-toggle collapsed" type="button" data-toggle="collapse" data-target=".bs-navbar-collapse">
				        <span class="sr-only">Toggle navigation</span>
				        <i class="fa fa-bars"></i>
				      </button>
				    </div>
				</div>
				<div class="col-md-8" id="menu">
				
					
					<div class="row">
					<nav class="collapse navbar-collapse bs-navbar-collapse" role="navigation"  style="border: 0px;">
				      <ul class="nav navbar-nav" style="  float: right; margin-top: 10px;">
				      						        <li >
					          <a href="/problems"><i class="fa fa-puzzle-piece"></i> PROBLEMS</a>
					        </li>
					        					        <li >
					          <a href="/status"><i class="fa fa-circle"></i> STATUS</a>
					        </li>
					        <li >
					          <a href="/ranks"><i class="fa fa-trophy"></i> RANKS</a>
					        </li>
					        <li >
					          <a href="http://spoj.com/forum"><i class="fa fa-comments-o"></i> DISCUSS</a>
					        </li>
					        <li >
					          <a href="/contests">CONTESTS</a>
					        </li>
											        					        
						        						      	
						      							      	<li style="margin-right: 0px;">
						      		<a href="/manageaccount/">
						      			<span tabindex="0" id="profile-menu" data-trigger="hover" data-container="body" data-toggle="popover" data-html="true" data-placement="left" data-content="You filled 50% of your profile, maybe you want to add some more?"><i class="fa fa-exclamation-triangle text-danger"></i></span>
						      		</a>
						      	</li>
						      						        
					        <li class="dropdown profile">
					        	<a href="#" class="username_dropdown dropdown-toggle" data-toggle="dropdown">
					        		<img width="20" height="20" src="https://www.gravatar.com/avatar/d41d8cd98f00b204e9800998ecf8427e&s=20?20190217" class="avatar small-left-margin"/>
					        		<!-- itactuk -->PROFILE&nbsp;<span class="caret"></span>
					        	</a>	
			
									<ul class="dropdown-menu text-right pull-right" role="menu" aria-labelledby="dropdownUser">
										<li role="presentation"><a role="menuitem" tabindex="-1" href="/myaccount"><span class="fa fa-user fa-fw"></span>&nbsp; My profile</a></li>
										<li role="presentation"><a role="menuitem" tabindex="-1" href="/manageaccount"><span class="fa fa-cogs fa-fw"></span>&nbsp; Manage profile</a></li>
										<li role="presentation"><a role="menuitem" tabindex="-1" href="/status/itactuk"><span class="fa fa-history fa-fw"></span>&nbsp; Submissions history</a></li>
										<li class="divider"></li>
										<li role="presentation"><a role="menuitem" tabindex="-1" href="/logout"><span class="fa fa-sign-out fa-fw"></span>&nbsp; Sign out</a></li>
									</ul>
								
					        </li>
					        
					        						
				        
				      </ul>
				    </nav>
				    </div>
				    
				    
				</div>
			</div>
			
		</div>
		
		<div class="container" id="menu">
			
		</div>
		
		<div class="container" id="content">
		<div class="submenu">
	<ol class="">
			<li>Profile</li>
				</ol>
	
	<ol class="navbar-right">
								<li><a href="/status/kosaksi/">History of submissions</a></li>
		<li>(<a href="/status/kosaksi/signedlist/">plaintext version</a>)</li>
	</ol>
	
</div>

<div>
<div class="row">
	<div class="col-md-3" id="user-profile-left">
		<img  class="img-thumbnail" width="100%" style="max-width: 262px;" src="https://www.gravatar.com/avatar/04372dba130f0a8d051649661542ed68?s=290&20190217" class="avatar small-left-margin">
		<h3>Kousshik Raj</h3>		<h4>@kosaksi</h4>
		<p><i class="fa fa-map-marker"></i> India, Kharagpur</p>		<p><i class="fa fa-clock-o"></i> Joined Sep 2017</p>
		<p><i class="fa fa-trophy"></i> World Rank: #28304 (0.6 points)</p>
		<p><i class="fa fa-building-o "></i> Institution: IIT Kharagpur</p>				
		
		
			</div>
	<div class="col-md-9">
	
		<center>
		
		</center>
	
						<div class="row row-centered">
			<div class="col-md-12">
				<h3>Activity over the last year</h3>
				<div class="top-4 col-centered" id="cal-heatmap"></div>

				<h3 class="top-4">Effectiveness</h3>
				<div class="row">
					<div class="col-md-6 text-center valign-center">
						<dl class="dl-horizontal profile-info-data profile-info-data-stats">
							<dt><span class="fa fa-check fa-fw"></span>&nbsp;Problems solved</dt>
								<dd>70</dd>
							<dt><span class="fa fa-send fa-fw"></span>&nbsp;Solutions submitted</dt>
								<dd>105</dd>
						</dl>
					</div>
					<div class="col-md-6">
						<div id="chart_div"></div>
					</div>
				</div>
				
				<script type="text/javascript">
					function BackTime(date) {
						var y = date.getFullYear(),
							m = date.getMonth();
						return new Date(y-1, m+1, 15);
					}
					
					function drawChart() {

						var data = new google.visualization.DataTable();
							data.addColumn('string', '?');
							data.addColumn('number', 'ACC');
							data.addColumn('number', 'WA');
							data.addColumn('number', 'TLE');
							data.addColumn('number', 'RE');
							data.addColumn('number', 'CE');
							data.addRows([
							
							['Submissions', 70, 27, 3, 2, 3]
							
						]);
	
						var options = {
							isStacked: 'percent',
							pieSliceText: 'label',
							colors: ['#348d34', '#ec971f', '#ec971f', '#c9302c', '#c9302c'],
							//colors:['#00C030','#F09A24','#F09A24','#F09A24','#F09A24'],
							'width':400,
							'height':100,
							chartArea:{left:10,top:10,width:'90%',height:'90%'},
							fontName: '@font-family-base',
							legend: {
								position: 'top',
								textStyle: {
									fontName: '@font-family-base',
									bold: true
							}},
							hAxis: {
					            minValue: 0,
					            ticks: [0, .25, .5, .75, 1]
					          }
						};
	
						var chart = new google.visualization.BarChart(document.getElementById('chart_div'));
						chart.draw(data, options);
					}
					
					$(document).ready(function(){
					
						var cal = new CalHeatMap();
						cal.init({
							domain: "month",
							subDomain: "day",
							domainGutter: 3,
							tooltip: true,
							start: BackTime(new Date()),
							maxDate: new Date(),
							colLimit: 4,
							legend: [10, 20, 30, 40],
							itemName: ["submission", "submissions"],
							data: '/calendar/?ajax=1&uid=540353&start={{d:start}}&stop={{d:end}}'
						});
					});
					
					google.load('visualization', '1.0', {'packages':['corechart']});
					google.setOnLoadCallback(drawChart);
				</script>
				
				
						
			</div>
		</div>

		<h3 class="top-4 text-center">Problems</h3>
		<div class="row row-centered" id="user-profile-tables">
			<div class="col-md-12">
				<h4>List of solved classical problems:</h4>
				<table class="table table-condensed">
								<tr>
				<td align="left" width="14%"><a href="/status/ABSYS,kosaksi/">ABSYS</a></td>
				<td align="left" width="14%"><a href="/status/ARITH2,kosaksi/">ARITH2</a></td>
				<td align="left" width="14%"><a href="/status/CANTON,kosaksi/">CANTON</a></td>
				<td align="left" width="14%"><a href="/status/FCTRL2,kosaksi/">FCTRL2</a></td>
				<td align="left" width="14%"><a href="/status/INVCNT,kosaksi/">INVCNT</a></td>
				<td align="left" width="14%"><a href="/status/NY10A,kosaksi/">NY10A</a></td>
				<td align="left" width="14%"><a href="/status/PT07Z,kosaksi/">PT07Z</a></td>
				</tr>
								<tr>
				<td align="left" width="14%"><a href="/status/ACODE,kosaksi/">ACODE</a></td>
				<td align="left" width="14%"><a href="/status/ARMY,kosaksi/">ARMY</a></td>
				<td align="left" width="14%"><a href="/status/COINS,kosaksi/">COINS</a></td>
				<td align="left" width="14%"><a href="/status/FENCE1,kosaksi/">FENCE1</a></td>
				<td align="left" width="14%"><a href="/status/JULKA,kosaksi/">JULKA</a></td>
				<td align="left" width="14%"><a href="/status/OFFSIDE,kosaksi/">OFFSIDE</a></td>
				<td align="left" width="14%"><a href="/status/SAMER08F,kosaksi/">SAMER08F</a></td>
				</tr>
								<tr>
				<td align="left" width="14%"><a href="/status/ACPC10A,kosaksi/">ACPC10A</a></td>
				<td align="left" width="14%"><a href="/status/ARRAYSUB,kosaksi/">ARRAYSUB</a></td>
				<td align="left" width="14%"><a href="/status/CRDS,kosaksi/">CRDS</a></td>
				<td align="left" width="14%"><a href="/status/GIRLSNBS,kosaksi/">GIRLSNBS</a></td>
				<td align="left" width="14%"><a href="/status/LASTDIG,kosaksi/">LASTDIG</a></td>
				<td align="left" width="14%"><a href="/status/OLOLO,kosaksi/">OLOLO</a></td>
				<td align="left" width="14%"><a href="/status/SBANK,kosaksi/">SBANK</a></td>
				</tr>
								<tr>
				<td align="left" width="14%"><a href="/status/ADDREV,kosaksi/">ADDREV</a></td>
				<td align="left" width="14%"><a href="/status/BEENUMS,kosaksi/">BEENUMS</a></td>
				<td align="left" width="14%"><a href="/status/EASYPROB,kosaksi/">EASYPROB</a></td>
				<td align="left" width="14%"><a href="/status/GSS1,kosaksi/">GSS1</a></td>
				<td align="left" width="14%"><a href="/status/LASTDIG2,kosaksi/">LASTDIG2</a></td>
				<td align="left" width="14%"><a href="/status/ONP,kosaksi/">ONP</a></td>
				<td align="left" width="14%"><a href="/status/STAMPS,kosaksi/">STAMPS</a></td>
				</tr>
								<tr>
				<td align="left" width="14%"><a href="/status/AE00,kosaksi/">AE00</a></td>
				<td align="left" width="14%"><a href="/status/BISHOPS,kosaksi/">BISHOPS</a></td>
				<td align="left" width="14%"><a href="/status/EDIST,kosaksi/">EDIST</a></td>
				<td align="left" width="14%"><a href="/status/GSS3,kosaksi/">GSS3</a></td>
				<td align="left" width="14%"><a href="/status/MARBLES,kosaksi/">MARBLES</a></td>
				<td align="left" width="14%"><a href="/status/PALIN,kosaksi/">PALIN</a></td>
				<td align="left" width="14%"><a href="/status/STPAR,kosaksi/">STPAR</a></td>
				</tr>
								<tr>
				<td align="left" width="14%"><a href="/status/AGGRCOW,kosaksi/">AGGRCOW</a></td>
				<td align="left" width="14%"><a href="/status/BITMAP,kosaksi/">BITMAP</a></td>
				<td align="left" width="14%"><a href="/status/EIGHTS,kosaksi/">EIGHTS</a></td>
				<td align="left" width="14%"><a href="/status/HANGOVER,kosaksi/">HANGOVER</a></td>
				<td align="left" width="14%"><a href="/status/MAXLN,kosaksi/">MAXLN</a></td>
				<td align="left" width="14%"><a href="/status/PARTY,kosaksi/">PARTY</a></td>
				<td align="left" width="14%"><a href="/status/TEST,kosaksi/">TEST</a></td>
				</tr>
								<tr>
				<td align="left" width="14%"><a href="/status/AIBOHP,kosaksi/">AIBOHP</a></td>
				<td align="left" width="14%"><a href="/status/BUGLIFE,kosaksi/">BUGLIFE</a></td>
				<td align="left" width="14%"><a href="/status/ETF,kosaksi/">ETF</a></td>
				<td align="left" width="14%"><a href="/status/HORRIBLE,kosaksi/">HORRIBLE</a></td>
				<td align="left" width="14%"><a href="/status/MIXTURES,kosaksi/">MIXTURES</a></td>
				<td align="left" width="14%"><a href="/status/PERMUT2,kosaksi/">PERMUT2</a></td>
				<td align="left" width="14%"><a href="/status/TOANDFRO,kosaksi/">TOANDFRO</a></td>
				</tr>
								<tr>
				<td align="left" width="14%"><a href="/status/AMR10G,kosaksi/">AMR10G</a></td>
				<td align="left" width="14%"><a href="/status/BYTESM2,kosaksi/">BYTESM2</a></td>
				<td align="left" width="14%"><a href="/status/FARIDA,kosaksi/">FARIDA</a></td>
				<td align="left" width="14%"><a href="/status/HOTELS,kosaksi/">HOTELS</a></td>
				<td align="left" width="14%"><a href="/status/NGM,kosaksi/">NGM</a></td>
				<td align="left" width="14%"><a href="/status/PIGBANK,kosaksi/">PIGBANK</a></td>
				<td align="left" width="14%"><a href="/status/TRICOUNT,kosaksi/">TRICOUNT</a></td>
				</tr>
								<tr>
				<td align="left" width="14%"><a href="/status/ANARC09A,kosaksi/">ANARC09A</a></td>
				<td align="left" width="14%"><a href="/status/CANDY,kosaksi/">CANDY</a></td>
				<td align="left" width="14%"><a href="/status/FASHION,kosaksi/">FASHION</a></td>
				<td align="left" width="14%"><a href="/status/HPYNOS,kosaksi/">HPYNOS</a></td>
				<td align="left" width="14%"><a href="/status/NHAY,kosaksi/">NHAY</a></td>
				<td align="left" width="14%"><a href="/status/PRIME1,kosaksi/">PRIME1</a></td>
				<td align="left" width="14%"><a href="/status/TRT,kosaksi/">TRT</a></td>
				</tr>
								<tr>
				<td align="left" width="14%"><a href="/status/AP2,kosaksi/">AP2</a></td>
				<td align="left" width="14%"><a href="/status/CANDY3,kosaksi/">CANDY3</a></td>
				<td align="left" width="14%"><a href="/status/FCTRL,kosaksi/">FCTRL</a></td>
				<td align="left" width="14%"><a href="/status/HUBULLU,kosaksi/">HUBULLU</a></td>
				<td align="left" width="14%"><a href="/status/NSTEPS,kosaksi/">NSTEPS</a></td>
				<td align="left" width="14%"><a href="/status/PT07Y,kosaksi/">PT07Y</a></td>
				<td align="left" width="14%"><a href="/status/WILLITST,kosaksi/">WILLITST</a></td>
				</tr>
								</table>
				
				
								
							</div>
		</div>
	
	
	
	</div>
</div>
</div>








<table cellspacing="10" align="center">





</table>


	<br/>
</div>
		
		
		<div class="container" id="footer">
			<div class="row">
				<div class="col-md-10">
					<p><a href="/info">About</a> | <a href="/tutorials">Tutorial</a> | <a href="/tools">Tools</a> | <a href="/clusters">Clusters</a> | <a href="/credits">Credits</a> | <a href="/sphereengine">API</a> | <a href="/sphereengine-widget">Widgets</a></p>
					<p>Legal: 
					   <a href="/legal-tos/" target="_blank">Terms of Service</a> | <a href="/legal-pp/" target="_blank">Privacy Policy</a> | <a href="/legal-gdpr/" target="_blank">GDPR Info</a>
					</p>
				</div>
				<div class="col-md-2 text-right">
					<a href="/rss/" ><img src="//stx1.spoj.com/gfx/rss10x10.gif" border=0>&nbsp;RSS</a>&nbsp;
				</div>
			</div>
		</div>
		
		<div class="text-center" id="footer-srl">
			
	&copy; Spoj.com. All Rights Reserved. Spoj uses <a href="http://sphere-engine.com?utm_campaign=permanent&amp;utm_medium=footer&amp;utm_source=spoj" style="color:black">Sphere Engine</a>&trade; &copy; by <a href="http://sphere-research.com?utm_campaign=permanent&amp;utm_medium=footer&amp;utm_source=spoj" style="color:black">Sphere Research Labs</a>.

		</div> 
	</div>

	<!-- JavaScripts -->
	
		
	
	<script type="text/javascript">
	$(function(){
		setTimeout(function(){
			$('.no_a_info').css('visibility', 'visible');
		}, 5000);
		
		if(!$('.aProblemTop').length && !$('.aProblemsTop').length && !$('.aSubmitTop').length && !$('.aStatusTop').length && !$('.aMainRight').length){
			ga('send', 'event', 'ads', 'no-ads', 'main-contest');
		}
		if ($('.aProblemTop').height() == 0){
			$('.aProblemTop').css({'border': '1px solid #ddd', 'background': '#f0f4e3', 'height': 90});
			$('.aProblemTop').html($('<p class="text-center">using adblock?</p><h4 class="text-center">Online ads help us to maintain site.</h4><p class="text-center"><strong>please whitelist *.spoj.com</strong></p>'));
			ga('send', 'event', 'ads', 'adblock2', 'aProblemTop');
		}
		if ($('.aProblemsTop').height() == 0){
			ga('send', 'event', 'ads', 'adblock2', 'aProblemsTop');
		}
		if ($('.aSubmitTop').height() == 0){
			ga('send', 'event', 'ads', 'adblock2', 'aSubmitTop');
		}
		if ($('.aStatusTop').height() == 0){
			ga('send', 'event', 'ads', 'adblock2', 'aStatusTop');
		}
		if ($('.aMainRight').height() == 0){
			ga('send', 'event', 'ads', 'adblock2', 'aMainRight');
		}
	});
	</script>
	
	
	<script type="text/javascript" src="//stx1.spoj.com/gfx/jquery.timers.js"></script>
	<script type="text/javascript" src="//stx1.spoj.com/gfx/jquery.cookie.js"></script>
	
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>

	<script src="//stx1.spoj.com/gfx/md5.js"></script>
	<script src="//stx1.spoj.com/gfx/bootstrap-tour/build/js/bootstrap-tour.min.js"></script>
	<script src="//stx1.spoj.com/gfx/scripts/tour.js"></script>
	
	
	<div id="fb-root"></div>
	<script>(function(d, s, id) {
	  var js, fjs = d.getElementsByTagName(s)[0];
	  if (d.getElementById(id)) return;
	  js = d.createElement(s); js.id = id;
	  js.src = "//connect.facebook.net/pl_PL/sdk.js#xfbml=1&appId=321676846207&version=v2.0";
	  fjs.parentNode.insertBefore(js, fjs);
	}(document, 'script', 'facebook-jssdk'));</script>
	
	


<script>
	  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
	  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
	  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
	  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');
	  ga('create', 'UA-10507872-1', 'auto');
	  ga('require', 'linkid', 'linkid.js');
	  ga('send', 'pageview');
	</script>
<!-- Hotjar Tracking Code for http://www.spoj.com -->
<script>
    (function(h,o,t,j,a,r){
        h.hj=h.hj||function(){(h.hj.q=h.hj.q||[]).push(arguments)};
        h._hjSettings={hjid:334656,hjsv:5};
        a=o.getElementsByTagName('head')[0];
        r=o.createElement('script');r.async=1;
        r.src=t+h._hjSettings.hjid+j+h._hjSettings.hjsv;
        a.appendChild(r);
    })(window,document,'//static.hotjar.com/c/hotjar-','.js?sv=');
</script>
<script src="//m.servedby-buysellads.com/monetization.js" type="text/javascript"></script>
<script>
(function(){
  if(typeof _bsa !== 'undefined' && _bsa) {
    // format, zoneKey, segment:value, options
    _bsa.init('flexbar', 'CK7D4KJL', 'placement:demo');
  }
})();
</script>
<script type="text/javascript">
	$(function(){
		$(document).on('click', '.track', function(){
			var event = $(this).attr('data-event');
			var action = $(this).attr('data-action');
			var value = $(this).attr('data-value');
			ga('send', 'event', event, action, value);
		});
	});
	//window.open('http://incoming.hotjar.com/s/7366', '_blank');
	</script>


</body>
</html>"""
