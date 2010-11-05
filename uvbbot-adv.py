
    

  

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
  <head>
    <meta http-equiv="content-type" content="text/html;charset=UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="chrome=1">
        <title>uvbbot-adv.py at master from bobschriver's UVB-Python-Bot - GitHub</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub" />
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub" />

    <link href="https://assets1.github.com/stylesheets/bundle_common.css?94b2d09e9a7ab2667d0731c6255d63c907ac01a5" media="screen" rel="stylesheet" type="text/css" />
<link href="https://assets0.github.com/stylesheets/bundle_github.css?94b2d09e9a7ab2667d0731c6255d63c907ac01a5" media="screen" rel="stylesheet" type="text/css" />

    <script type="text/javascript" charset="utf-8">
      var GitHub = {}
      var github_user = null
      
    </script>
    <script src="https://assets2.github.com/javascripts/jquery/jquery-1.4.2.min.js?94b2d09e9a7ab2667d0731c6255d63c907ac01a5" type="text/javascript"></script>
    <script src="https://assets3.github.com/javascripts/bundle_common.js?94b2d09e9a7ab2667d0731c6255d63c907ac01a5" type="text/javascript"></script>
<script src="https://assets3.github.com/javascripts/bundle_github.js?94b2d09e9a7ab2667d0731c6255d63c907ac01a5" type="text/javascript"></script>

        <script type="text/javascript" charset="utf-8">
      GitHub.spy({
        repo: "bobschriver/UVB-Python-Bot"
      })
    </script>

    
  
    
  

  <link href="https://github.com/bobschriver/UVB-Python-Bot/commits/master.atom" rel="alternate" title="Recent Commits to UVB-Python-Bot:master" type="application/atom+xml" />

        <meta name="description" content="UVB AI Bot written in python" />
    <script type="text/javascript">
      GitHub.nameWithOwner = GitHub.nameWithOwner || "bobschriver/UVB-Python-Bot";
      GitHub.currentRef = 'master';
    </script>
  

            <script type="text/javascript">
      var _gaq = _gaq || [];
      _gaq.push(['_setAccount', 'UA-3769691-2']);
      _gaq.push(['_trackPageview']);
      (function() {
        var ga = document.createElement('script');
        ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
        ga.setAttribute('async', 'true');
        document.documentElement.firstChild.appendChild(ga);
      })();
    </script>

  </head>

  

  <body class="logged_out ">
    

    
      <script type="text/javascript">
        var _kmq = _kmq || [];
        function _kms(u){
          var s = document.createElement('script'); var f = document.getElementsByTagName('script')[0]; s.type = 'text/javascript'; s.async = true;
          s.src = u; f.parentNode.insertBefore(s, f);
        }
        _kms('//i.kissmetrics.com/i.js');_kms('//doug1izaerwt3.cloudfront.net/406e8bf3a2b8846ead55afb3cfaf6664523e3a54.1.js');
      </script>
    

    

    

    

    <div class="subnavd" id="main">
      <div id="header" class="true">
        
          <a class="logo boring" href="https://github.com">
            <img src="/images/modules/header/logov3.png?changed" class="default" alt="github" />
            <![if !IE]>
            <img src="/images/modules/header/logov3-hover.png" class="hover" alt="github" />
            <![endif]>
          </a>
        
        
        <div class="topsearch">
  
    <ul class="nav logged_out">
      <li><a href="https://github.com">Home</a></li>
      <li class="pricing"><a href="/plans">Pricing and Signup</a></li>
      <li><a href="https://github.com/training">Training</a></li>
      <li><a href="https://gist.github.com">Gist</a></li>
      <li><a href="/blog">Blog</a></li>
      <li><a href="https://github.com/login">Login</a></li>
    </ul>
  
</div>

      </div>

      
      
        
    <div class="site">
      <div class="pagehead repohead vis-public   ">

      

      <div class="title-actions-bar">
        <h1>
          <a href="/bobschriver">bobschriver</a> / <strong><a href="https://github.com/bobschriver/UVB-Python-Bot">UVB-Python-Bot</a></strong>
          
          
        </h1>

        
    <ul class="actions">
      

      
        <li class="for-owner" style="display:none"><a href="https://github.com/bobschriver/UVB-Python-Bot/admin" class="minibutton btn-admin "><span><span class="icon"></span>Admin</span></a></li>
        <li>
          <a href="/bobschriver/UVB-Python-Bot/toggle_watch" class="minibutton btn-watch " id="watch_button" onclick="var f = document.createElement('form'); f.style.display = 'none'; this.parentNode.appendChild(f); f.method = 'POST'; f.action = this.href;var s = document.createElement('input'); s.setAttribute('type', 'hidden'); s.setAttribute('name', 'authenticity_token'); s.setAttribute('value', 'c7d1cd86b87e139668d9306efe0c18637dae9447'); f.appendChild(s);f.submit();return false;" style="display:none"><span><span class="icon"></span>Watch</span></a>
          <a href="/bobschriver/UVB-Python-Bot/toggle_watch" class="minibutton btn-watch " id="unwatch_button" onclick="var f = document.createElement('form'); f.style.display = 'none'; this.parentNode.appendChild(f); f.method = 'POST'; f.action = this.href;var s = document.createElement('input'); s.setAttribute('type', 'hidden'); s.setAttribute('name', 'authenticity_token'); s.setAttribute('value', 'c7d1cd86b87e139668d9306efe0c18637dae9447'); f.appendChild(s);f.submit();return false;" style="display:none"><span><span class="icon"></span>Unwatch</span></a>
        </li>
        
          
            <li class="for-notforked" style="display:none"><a href="/bobschriver/UVB-Python-Bot/fork" class="minibutton btn-fork " id="fork_button" onclick="var f = document.createElement('form'); f.style.display = 'none'; this.parentNode.appendChild(f); f.method = 'POST'; f.action = this.href;var s = document.createElement('input'); s.setAttribute('type', 'hidden'); s.setAttribute('name', 'authenticity_token'); s.setAttribute('value', 'c7d1cd86b87e139668d9306efe0c18637dae9447'); f.appendChild(s);f.submit();return false;"><span><span class="icon"></span>Fork</span></a></li>
            <li class="for-hasfork" style="display:none"><a href="#" class="minibutton btn-fork " id="your_fork_button"><span><span class="icon"></span>Your Fork</span></a></li>
          

          
        
      
      
      <li class="repostats">
        <ul class="repo-stats">
          <li class="watchers"><a href="/bobschriver/UVB-Python-Bot/watchers" title="Watchers" class="tooltipped downwards">2</a></li>
          <li class="forks"><a href="/bobschriver/UVB-Python-Bot/network" title="Forks" class="tooltipped downwards">1</a></li>
        </ul>
      </li>
    </ul>

      </div>

        
  <ul class="tabs">
    <li><a href="https://github.com/bobschriver/UVB-Python-Bot/tree/master" class="selected" highlight="repo_source">Source</a></li>
    <li><a href="https://github.com/bobschriver/UVB-Python-Bot/commits/master" highlight="repo_commits">Commits</a></li>
    <li><a href="/bobschriver/UVB-Python-Bot/network" highlight="repo_network">Network</a></li>
    <li><a href="/bobschriver/UVB-Python-Bot/pulls" highlight="repo_pulls">Pull Requests (0)</a></li>

    

    
      
      <li><a href="/bobschriver/UVB-Python-Bot/issues" highlight="issues">Issues (0)</a></li>
    

            
    <li><a href="/bobschriver/UVB-Python-Bot/graphs" highlight="repo_graphs">Graphs</a></li>

    <li class="contextswitch nochoices">
      <span class="toggle leftwards" >
        <em>Branch:</em>
        <code>master</code>
      </span>
    </li>
  </ul>

  <div style="display:none" id="pl-description"><p><em class="placeholder">click here to add a description</em></p></div>
  <div style="display:none" id="pl-homepage"><p><em class="placeholder">click here to add a homepage</em></p></div>

  <div class="subnav-bar">
  
  <ul>
    <li>
      <a href="#" class="dropdown">Switch Branches (2)</a>
      <ul>
        
          
          
            <li><a href="/bobschriver/UVB-Python-Bot/blob/deliberate/uvbbot-adv.py" action="show">deliberate</a></li>
          
        
          
            <li><strong>master &#x2713;</strong></li>
            
      </ul>
    </li>
    <li>
      <a href="#" class="dropdown defunct">Switch Tags (0)</a>
      
    </li>
    <li>
    
    <a href="/bobschriver/UVB-Python-Bot/branches" class="manage">Branch List</a>
    
    </li>
  </ul>
</div>

  
  
  
  
  
  



        
    <div id="repo_details" class="metabox clearfix">
      <div id="repo_details_loader" class="metabox-loader" style="display:none">Sending Request&hellip;</div>

        <a href="/bobschriver/UVB-Python-Bot/downloads" class="download-source" id="download_button" title="Download source, tagged packages and binaries."><span class="icon"></span>Downloads</a>

      <div id="repository_desc_wrapper">
      <div id="repository_description" rel="repository_description_edit">
        
          <p>UVB AI Bot written in python
            <span id="read_more" style="display:none">&mdash; <a href="#readme">Read more</a></span>
          </p>
        
      </div>

      <div id="repository_description_edit" style="display:none;" class="inline-edit">
        <form action="/bobschriver/UVB-Python-Bot/admin/update" method="post"><div style="margin:0;padding:0"><input name="authenticity_token" type="hidden" value="c7d1cd86b87e139668d9306efe0c18637dae9447" /></div>
          <input type="hidden" name="field" value="repository_description">
          <input type="text" class="textfield" name="value" value="UVB AI Bot written in python">
          <div class="form-actions">
            <button class="minibutton"><span>Save</span></button> &nbsp; <a href="#" class="cancel">Cancel</a>
          </div>
        </form>
      </div>

      
      <div class="repository-homepage" id="repository_homepage" rel="repository_homepage_edit">
        <p><a href="http://" rel="nofollow"></a></p>
      </div>

      <div id="repository_homepage_edit" style="display:none;" class="inline-edit">
        <form action="/bobschriver/UVB-Python-Bot/admin/update" method="post"><div style="margin:0;padding:0"><input name="authenticity_token" type="hidden" value="c7d1cd86b87e139668d9306efe0c18637dae9447" /></div>
          <input type="hidden" name="field" value="repository_homepage">
          <input type="text" class="textfield" name="value" value="">
          <div class="form-actions">
            <button class="minibutton"><span>Save</span></button> &nbsp; <a href="#" class="cancel">Cancel</a>
          </div>
        </form>
      </div>
      </div>
      <div class="rule "></div>
            <div id="url_box" class="url-box">
        <ul class="clone-urls">
          
            
            <li id="http_clone_url"><a href="https://github.com/bobschriver/UVB-Python-Bot.git" data-permissions="Read-Only">HTTP</a></li>
            <li id="public_clone_url"><a href="git://github.com/bobschriver/UVB-Python-Bot.git" data-permissions="Read-Only">Git Read-Only</a></li>
          
        </ul>
        <input type="text" spellcheck="false" id="url_field" class="url-field" />
              <span style="display:none" id="url_box_clippy"></span>
      <span id="clippy_tooltip_url_box_clippy" class="clippy-tooltip tooltipped" title="copy to clipboard">
      <object classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000"
              width="14"
              height="14"
              class="clippy"
              id="clippy" >
      <param name="movie" value="https://assets2.github.com/flash/clippy.swf?v5"/>
      <param name="allowScriptAccess" value="always" />
      <param name="quality" value="high" />
      <param name="scale" value="noscale" />
      <param NAME="FlashVars" value="id=url_box_clippy&amp;copied=&amp;copyto=">
      <param name="bgcolor" value="#FFFFFF">
      <param name="wmode" value="opaque">
      <embed src="https://assets2.github.com/flash/clippy.swf?v5"
             width="14"
             height="14"
             name="clippy"
             quality="high"
             allowScriptAccess="always"
             type="application/x-shockwave-flash"
             pluginspage="http://www.macromedia.com/go/getflashplayer"
             FlashVars="id=url_box_clippy&amp;copied=&amp;copyto="
             bgcolor="#FFFFFF"
             wmode="opaque"
      />
      </object>
      </span>

        <p id="url_description">This URL has <strong>Read+Write</strong> access</p>
      </div>
    </div>


        

      </div><!-- /.pagehead -->

      









<script type="text/javascript">
  GitHub.currentCommitRef = 'master'
  GitHub.currentRepoOwner = 'bobschriver'
  GitHub.currentRepo = "UVB-Python-Bot"
  GitHub.downloadRepo = '/bobschriver/UVB-Python-Bot/archives/master'
  GitHub.revType = "master"

  GitHub.controllerName = "blob"
  GitHub.actionName     = "show"
  GitHub.currentAction  = "blob#show"

  

  
</script>








  <div id="commit">
    <div class="group">
        
  <div class="envelope commit">
    <div class="human">
      
        <div class="message"><pre><a href="/bobschriver/UVB-Python-Bot/commit/c7af262deae127b39ea09e0fd87ed0b362c3ebcb">Fixed some snowball tracking issues</a> </pre></div>
      

      <div class="actor">
        <div class="gravatar">
          
          <img src="https://secure.gravatar.com/avatar/56e840c3782f95e36faa85a09b80abdc?s=140&d=https%3A%2F%2Fgithub.com%2Fimages%2Fgravatars%2Fgravatar-140.png" alt="" width="30" height="30"  />
        </div>
        <div class="name">Robert Schriver <span>(author)</span></div>
        <div class="date">
          <abbr class="relatize" title="2010-11-04 13:01:14">Thu Nov 04 13:01:14 -0700 2010</abbr>
        </div>
      </div>

      

    </div>
    <div class="machine">
      <span>c</span>ommit&nbsp;&nbsp;<a href="/bobschriver/UVB-Python-Bot/commit/c7af262deae127b39ea09e0fd87ed0b362c3ebcb" hotkey="c">c7af262deae127b39ea0</a><br />
      <span>t</span>ree&nbsp;&nbsp;&nbsp;&nbsp;<a href="/bobschriver/UVB-Python-Bot/tree/c7af262deae127b39ea09e0fd87ed0b362c3ebcb" hotkey="t">7e02563f1296a411fb22</a><br />
      
        <span>p</span>arent&nbsp;
        
        <a href="/bobschriver/UVB-Python-Bot/tree/d249c10d460698b5daaae7782cd0f95e0bace51d" hotkey="p">d249c10d460698b5daaa</a>
      

    </div>
  </div>

    </div>
  </div>



  
    <div id="path">
      <b><a href="/bobschriver/UVB-Python-Bot/tree/master">UVB-Python-Bot</a></b> / uvbbot-adv.py       <span style="display:none" id="clippy_422">uvbbot-adv.py</span>
      
      <object classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000"
              width="110"
              height="14"
              class="clippy"
              id="clippy" >
      <param name="movie" value="https://assets2.github.com/flash/clippy.swf?v5"/>
      <param name="allowScriptAccess" value="always" />
      <param name="quality" value="high" />
      <param name="scale" value="noscale" />
      <param NAME="FlashVars" value="id=clippy_422&amp;copied=copied!&amp;copyto=copy to clipboard">
      <param name="bgcolor" value="#FFFFFF">
      <param name="wmode" value="opaque">
      <embed src="https://assets2.github.com/flash/clippy.swf?v5"
             width="110"
             height="14"
             name="clippy"
             quality="high"
             allowScriptAccess="always"
             type="application/x-shockwave-flash"
             pluginspage="http://www.macromedia.com/go/getflashplayer"
             FlashVars="id=clippy_422&amp;copied=copied!&amp;copyto=copy to clipboard"
             bgcolor="#FFFFFF"
             wmode="opaque"
      />
      </object>
      

    </div>

    <div id="files">
      <div class="file">
        <div class="meta">
          <div class="info">
            <span class="icon"><img alt="Txt" height="16" src="https://assets3.github.com/images/icons/txt.png?94b2d09e9a7ab2667d0731c6255d63c907ac01a5" width="16" /></span>
            <span class="mode" title="File Mode">100644</span>
            
              <span>274 lines (206 sloc)</span>
            
            <span>7.723 kb</span>
          </div>
          <ul class="actions">
            
              <li><a id="file-edit-link" href="#" rel="/bobschriver/UVB-Python-Bot/file-edit/__ref__/uvbbot-adv.py">edit</a></li>
            
            <li><a href="/bobschriver/UVB-Python-Bot/raw/master/uvbbot-adv.py" id="raw-url">raw</a></li>
            
              <li><a href="/bobschriver/UVB-Python-Bot/blame/master/uvbbot-adv.py">blame</a></li>
            
            <li><a href="/bobschriver/UVB-Python-Bot/commits/master/uvbbot-adv.py">history</a></li>
          </ul>
        </div>
        
  <div class="data type-python">
    
      <table cellpadding="0" cellspacing="0">
        <tr>
          <td>
            <pre class="line_numbers"><span id="LID1" rel="#L1">1</span>
<span id="LID2" rel="#L2">2</span>
<span id="LID3" rel="#L3">3</span>
<span id="LID4" rel="#L4">4</span>
<span id="LID5" rel="#L5">5</span>
<span id="LID6" rel="#L6">6</span>
<span id="LID7" rel="#L7">7</span>
<span id="LID8" rel="#L8">8</span>
<span id="LID9" rel="#L9">9</span>
<span id="LID10" rel="#L10">10</span>
<span id="LID11" rel="#L11">11</span>
<span id="LID12" rel="#L12">12</span>
<span id="LID13" rel="#L13">13</span>
<span id="LID14" rel="#L14">14</span>
<span id="LID15" rel="#L15">15</span>
<span id="LID16" rel="#L16">16</span>
<span id="LID17" rel="#L17">17</span>
<span id="LID18" rel="#L18">18</span>
<span id="LID19" rel="#L19">19</span>
<span id="LID20" rel="#L20">20</span>
<span id="LID21" rel="#L21">21</span>
<span id="LID22" rel="#L22">22</span>
<span id="LID23" rel="#L23">23</span>
<span id="LID24" rel="#L24">24</span>
<span id="LID25" rel="#L25">25</span>
<span id="LID26" rel="#L26">26</span>
<span id="LID27" rel="#L27">27</span>
<span id="LID28" rel="#L28">28</span>
<span id="LID29" rel="#L29">29</span>
<span id="LID30" rel="#L30">30</span>
<span id="LID31" rel="#L31">31</span>
<span id="LID32" rel="#L32">32</span>
<span id="LID33" rel="#L33">33</span>
<span id="LID34" rel="#L34">34</span>
<span id="LID35" rel="#L35">35</span>
<span id="LID36" rel="#L36">36</span>
<span id="LID37" rel="#L37">37</span>
<span id="LID38" rel="#L38">38</span>
<span id="LID39" rel="#L39">39</span>
<span id="LID40" rel="#L40">40</span>
<span id="LID41" rel="#L41">41</span>
<span id="LID42" rel="#L42">42</span>
<span id="LID43" rel="#L43">43</span>
<span id="LID44" rel="#L44">44</span>
<span id="LID45" rel="#L45">45</span>
<span id="LID46" rel="#L46">46</span>
<span id="LID47" rel="#L47">47</span>
<span id="LID48" rel="#L48">48</span>
<span id="LID49" rel="#L49">49</span>
<span id="LID50" rel="#L50">50</span>
<span id="LID51" rel="#L51">51</span>
<span id="LID52" rel="#L52">52</span>
<span id="LID53" rel="#L53">53</span>
<span id="LID54" rel="#L54">54</span>
<span id="LID55" rel="#L55">55</span>
<span id="LID56" rel="#L56">56</span>
<span id="LID57" rel="#L57">57</span>
<span id="LID58" rel="#L58">58</span>
<span id="LID59" rel="#L59">59</span>
<span id="LID60" rel="#L60">60</span>
<span id="LID61" rel="#L61">61</span>
<span id="LID62" rel="#L62">62</span>
<span id="LID63" rel="#L63">63</span>
<span id="LID64" rel="#L64">64</span>
<span id="LID65" rel="#L65">65</span>
<span id="LID66" rel="#L66">66</span>
<span id="LID67" rel="#L67">67</span>
<span id="LID68" rel="#L68">68</span>
<span id="LID69" rel="#L69">69</span>
<span id="LID70" rel="#L70">70</span>
<span id="LID71" rel="#L71">71</span>
<span id="LID72" rel="#L72">72</span>
<span id="LID73" rel="#L73">73</span>
<span id="LID74" rel="#L74">74</span>
<span id="LID75" rel="#L75">75</span>
<span id="LID76" rel="#L76">76</span>
<span id="LID77" rel="#L77">77</span>
<span id="LID78" rel="#L78">78</span>
<span id="LID79" rel="#L79">79</span>
<span id="LID80" rel="#L80">80</span>
<span id="LID81" rel="#L81">81</span>
<span id="LID82" rel="#L82">82</span>
<span id="LID83" rel="#L83">83</span>
<span id="LID84" rel="#L84">84</span>
<span id="LID85" rel="#L85">85</span>
<span id="LID86" rel="#L86">86</span>
<span id="LID87" rel="#L87">87</span>
<span id="LID88" rel="#L88">88</span>
<span id="LID89" rel="#L89">89</span>
<span id="LID90" rel="#L90">90</span>
<span id="LID91" rel="#L91">91</span>
<span id="LID92" rel="#L92">92</span>
<span id="LID93" rel="#L93">93</span>
<span id="LID94" rel="#L94">94</span>
<span id="LID95" rel="#L95">95</span>
<span id="LID96" rel="#L96">96</span>
<span id="LID97" rel="#L97">97</span>
<span id="LID98" rel="#L98">98</span>
<span id="LID99" rel="#L99">99</span>
<span id="LID100" rel="#L100">100</span>
<span id="LID101" rel="#L101">101</span>
<span id="LID102" rel="#L102">102</span>
<span id="LID103" rel="#L103">103</span>
<span id="LID104" rel="#L104">104</span>
<span id="LID105" rel="#L105">105</span>
<span id="LID106" rel="#L106">106</span>
<span id="LID107" rel="#L107">107</span>
<span id="LID108" rel="#L108">108</span>
<span id="LID109" rel="#L109">109</span>
<span id="LID110" rel="#L110">110</span>
<span id="LID111" rel="#L111">111</span>
<span id="LID112" rel="#L112">112</span>
<span id="LID113" rel="#L113">113</span>
<span id="LID114" rel="#L114">114</span>
<span id="LID115" rel="#L115">115</span>
<span id="LID116" rel="#L116">116</span>
<span id="LID117" rel="#L117">117</span>
<span id="LID118" rel="#L118">118</span>
<span id="LID119" rel="#L119">119</span>
<span id="LID120" rel="#L120">120</span>
<span id="LID121" rel="#L121">121</span>
<span id="LID122" rel="#L122">122</span>
<span id="LID123" rel="#L123">123</span>
<span id="LID124" rel="#L124">124</span>
<span id="LID125" rel="#L125">125</span>
<span id="LID126" rel="#L126">126</span>
<span id="LID127" rel="#L127">127</span>
<span id="LID128" rel="#L128">128</span>
<span id="LID129" rel="#L129">129</span>
<span id="LID130" rel="#L130">130</span>
<span id="LID131" rel="#L131">131</span>
<span id="LID132" rel="#L132">132</span>
<span id="LID133" rel="#L133">133</span>
<span id="LID134" rel="#L134">134</span>
<span id="LID135" rel="#L135">135</span>
<span id="LID136" rel="#L136">136</span>
<span id="LID137" rel="#L137">137</span>
<span id="LID138" rel="#L138">138</span>
<span id="LID139" rel="#L139">139</span>
<span id="LID140" rel="#L140">140</span>
<span id="LID141" rel="#L141">141</span>
<span id="LID142" rel="#L142">142</span>
<span id="LID143" rel="#L143">143</span>
<span id="LID144" rel="#L144">144</span>
<span id="LID145" rel="#L145">145</span>
<span id="LID146" rel="#L146">146</span>
<span id="LID147" rel="#L147">147</span>
<span id="LID148" rel="#L148">148</span>
<span id="LID149" rel="#L149">149</span>
<span id="LID150" rel="#L150">150</span>
<span id="LID151" rel="#L151">151</span>
<span id="LID152" rel="#L152">152</span>
<span id="LID153" rel="#L153">153</span>
<span id="LID154" rel="#L154">154</span>
<span id="LID155" rel="#L155">155</span>
<span id="LID156" rel="#L156">156</span>
<span id="LID157" rel="#L157">157</span>
<span id="LID158" rel="#L158">158</span>
<span id="LID159" rel="#L159">159</span>
<span id="LID160" rel="#L160">160</span>
<span id="LID161" rel="#L161">161</span>
<span id="LID162" rel="#L162">162</span>
<span id="LID163" rel="#L163">163</span>
<span id="LID164" rel="#L164">164</span>
<span id="LID165" rel="#L165">165</span>
<span id="LID166" rel="#L166">166</span>
<span id="LID167" rel="#L167">167</span>
<span id="LID168" rel="#L168">168</span>
<span id="LID169" rel="#L169">169</span>
<span id="LID170" rel="#L170">170</span>
<span id="LID171" rel="#L171">171</span>
<span id="LID172" rel="#L172">172</span>
<span id="LID173" rel="#L173">173</span>
<span id="LID174" rel="#L174">174</span>
<span id="LID175" rel="#L175">175</span>
<span id="LID176" rel="#L176">176</span>
<span id="LID177" rel="#L177">177</span>
<span id="LID178" rel="#L178">178</span>
<span id="LID179" rel="#L179">179</span>
<span id="LID180" rel="#L180">180</span>
<span id="LID181" rel="#L181">181</span>
<span id="LID182" rel="#L182">182</span>
<span id="LID183" rel="#L183">183</span>
<span id="LID184" rel="#L184">184</span>
<span id="LID185" rel="#L185">185</span>
<span id="LID186" rel="#L186">186</span>
<span id="LID187" rel="#L187">187</span>
<span id="LID188" rel="#L188">188</span>
<span id="LID189" rel="#L189">189</span>
<span id="LID190" rel="#L190">190</span>
<span id="LID191" rel="#L191">191</span>
<span id="LID192" rel="#L192">192</span>
<span id="LID193" rel="#L193">193</span>
<span id="LID194" rel="#L194">194</span>
<span id="LID195" rel="#L195">195</span>
<span id="LID196" rel="#L196">196</span>
<span id="LID197" rel="#L197">197</span>
<span id="LID198" rel="#L198">198</span>
<span id="LID199" rel="#L199">199</span>
<span id="LID200" rel="#L200">200</span>
<span id="LID201" rel="#L201">201</span>
<span id="LID202" rel="#L202">202</span>
<span id="LID203" rel="#L203">203</span>
<span id="LID204" rel="#L204">204</span>
<span id="LID205" rel="#L205">205</span>
<span id="LID206" rel="#L206">206</span>
<span id="LID207" rel="#L207">207</span>
<span id="LID208" rel="#L208">208</span>
<span id="LID209" rel="#L209">209</span>
<span id="LID210" rel="#L210">210</span>
<span id="LID211" rel="#L211">211</span>
<span id="LID212" rel="#L212">212</span>
<span id="LID213" rel="#L213">213</span>
<span id="LID214" rel="#L214">214</span>
<span id="LID215" rel="#L215">215</span>
<span id="LID216" rel="#L216">216</span>
<span id="LID217" rel="#L217">217</span>
<span id="LID218" rel="#L218">218</span>
<span id="LID219" rel="#L219">219</span>
<span id="LID220" rel="#L220">220</span>
<span id="LID221" rel="#L221">221</span>
<span id="LID222" rel="#L222">222</span>
<span id="LID223" rel="#L223">223</span>
<span id="LID224" rel="#L224">224</span>
<span id="LID225" rel="#L225">225</span>
<span id="LID226" rel="#L226">226</span>
<span id="LID227" rel="#L227">227</span>
<span id="LID228" rel="#L228">228</span>
<span id="LID229" rel="#L229">229</span>
<span id="LID230" rel="#L230">230</span>
<span id="LID231" rel="#L231">231</span>
<span id="LID232" rel="#L232">232</span>
<span id="LID233" rel="#L233">233</span>
<span id="LID234" rel="#L234">234</span>
<span id="LID235" rel="#L235">235</span>
<span id="LID236" rel="#L236">236</span>
<span id="LID237" rel="#L237">237</span>
<span id="LID238" rel="#L238">238</span>
<span id="LID239" rel="#L239">239</span>
<span id="LID240" rel="#L240">240</span>
<span id="LID241" rel="#L241">241</span>
<span id="LID242" rel="#L242">242</span>
<span id="LID243" rel="#L243">243</span>
<span id="LID244" rel="#L244">244</span>
<span id="LID245" rel="#L245">245</span>
<span id="LID246" rel="#L246">246</span>
<span id="LID247" rel="#L247">247</span>
<span id="LID248" rel="#L248">248</span>
<span id="LID249" rel="#L249">249</span>
<span id="LID250" rel="#L250">250</span>
<span id="LID251" rel="#L251">251</span>
<span id="LID252" rel="#L252">252</span>
<span id="LID253" rel="#L253">253</span>
<span id="LID254" rel="#L254">254</span>
<span id="LID255" rel="#L255">255</span>
<span id="LID256" rel="#L256">256</span>
<span id="LID257" rel="#L257">257</span>
<span id="LID258" rel="#L258">258</span>
<span id="LID259" rel="#L259">259</span>
<span id="LID260" rel="#L260">260</span>
<span id="LID261" rel="#L261">261</span>
<span id="LID262" rel="#L262">262</span>
<span id="LID263" rel="#L263">263</span>
<span id="LID264" rel="#L264">264</span>
<span id="LID265" rel="#L265">265</span>
<span id="LID266" rel="#L266">266</span>
<span id="LID267" rel="#L267">267</span>
<span id="LID268" rel="#L268">268</span>
<span id="LID269" rel="#L269">269</span>
<span id="LID270" rel="#L270">270</span>
<span id="LID271" rel="#L271">271</span>
<span id="LID272" rel="#L272">272</span>
<span id="LID273" rel="#L273">273</span>
<span id="LID274" rel="#L274">274</span>
</pre>
          </td>
          <td width="100%">
            
              
                <div class="highlight"><pre><div class='line' id='LC1'><span class="c">#!/usr/bin/python</span></div><div class='line' id='LC2'><br/></div><div class='line' id='LC3'><span class="kn">from</span> <span class="nn">client</span> <span class="kn">import</span> <span class="n">Client</span></div><div class='line' id='LC4'><span class="kn">from</span> <span class="nn">constants</span> <span class="kn">import</span> <span class="n">Action</span><span class="p">,</span> <span class="n">Direction</span></div><div class='line' id='LC5'><span class="kn">import</span> <span class="nn">random</span></div><div class='line' id='LC6'><span class="kn">import</span> <span class="nn">math</span></div><div class='line' id='LC7'><span class="kn">import</span> <span class="nn">sys</span></div><div class='line' id='LC8'><br/></div><div class='line' id='LC9'><span class="c"># This function is called everytime the client gets a new map.</span></div><div class='line' id='LC10'><span class="c"># It decides what move to make and returns the decision.</span></div><div class='line' id='LC11'><span class="c"># The client module takes care of the network communication magic.</span></div><div class='line' id='LC12'><span class="k">def</span> <span class="nf">dummy</span><span class="p">(</span><span class="n">board</span><span class="p">):</span></div><div class='line' id='LC13'>	<span class="c"># We need this variable to keep state between moves</span></div><div class='line' id='LC14'>	<span class="k">global</span> <span class="n">curr_dir</span></div><div class='line' id='LC15'>	<span class="k">global</span> <span class="n">curr_loc</span></div><div class='line' id='LC16'><br/></div><div class='line' id='LC17'>	<span class="k">global</span> <span class="n">snowball_locs</span></div><div class='line' id='LC18'><br/></div><div class='line' id='LC19'>	<span class="k">global</span> <span class="n">snowballs</span></div><div class='line' id='LC20'>	<span class="k">global</span> <span class="n">min_snowballs</span></div><div class='line' id='LC21'>	<span class="k">global</span> <span class="n">max_snowballs</span></div><div class='line' id='LC22'><br/></div><div class='line' id='LC23'>	<span class="k">global</span> <span class="n">min_player_distance</span></div><div class='line' id='LC24'><br/></div><div class='line' id='LC25'>	<span class="k">global</span> <span class="n">max_throw_snowball_distance</span></div><div class='line' id='LC26'><br/></div><div class='line' id='LC27'>	<span class="c"># Print out our view of the game board</span></div><div class='line' id='LC28'>	<span class="k">print</span> <span class="n">board</span></div><div class='line' id='LC29'><br/></div><div class='line' id='LC30'>	<span class="n">possible_moves</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span></div><div class='line' id='LC31'><br/></div><div class='line' id='LC32'>	<span class="k">if</span> <span class="n">snowballs</span> <span class="o">&lt;</span> <span class="n">max_snowballs</span><span class="p">:</span></div><div class='line' id='LC33'>		<span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">max_snowballs</span> <span class="o">-</span> <span class="n">snowballs</span><span class="p">):</span></div><div class='line' id='LC34'>			<span class="n">possible_moves</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">Action</span><span class="o">.</span><span class="n">MAKESNOWBALL</span> <span class="p">,</span> <span class="n">curr_dir</span><span class="p">))</span></div><div class='line' id='LC35'><br/></div><div class='line' id='LC36'>	<span class="k">if</span> <span class="n">snowballs</span> <span class="o">&lt;</span> <span class="n">min_snowballs</span><span class="p">:</span></div><div class='line' id='LC37'>		<span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">math</span><span class="o">.</span><span class="n">pow</span><span class="p">(</span><span class="mi">2</span> <span class="p">,</span> <span class="n">min_snowballs</span> <span class="o">-</span> <span class="n">snowballs</span><span class="p">)):</span></div><div class='line' id='LC38'>			<span class="n">possible_moves</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">Action</span><span class="o">.</span><span class="n">MAKESNOWBALL</span> <span class="p">,</span> <span class="n">curr_dir</span><span class="p">))</span></div><div class='line' id='LC39'><br/></div><div class='line' id='LC40'>	<span class="n">possible_moves</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">Action</span><span class="o">.</span><span class="n">MAKESNOWBALL</span> <span class="p">,</span> <span class="n">curr_dir</span><span class="p">))</span></div><div class='line' id='LC41'><br/></div><div class='line' id='LC42'>	<span class="c">#replace with the curr_loc + direction at some point</span></div><div class='line' id='LC43'>	<span class="k">for</span> <span class="n">loc</span> <span class="ow">in</span> <span class="n">board</span><span class="o">.</span><span class="n">objects</span><span class="p">:</span></div><div class='line' id='LC44'>		<span class="k">if</span> <span class="n">board</span><span class="o">.</span><span class="n">get_object_at</span><span class="p">(</span><span class="n">loc</span><span class="p">)</span> <span class="o">==</span> <span class="n">board</span><span class="o">.</span><span class="n">ME</span><span class="p">:</span></div><div class='line' id='LC45'>			<span class="n">curr_loc</span> <span class="o">=</span> <span class="nb">eval</span><span class="p">(</span><span class="n">loc</span><span class="p">)</span>		</div><div class='line' id='LC46'><br/></div><div class='line' id='LC47'>	<span class="n">player_locs</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span></div><div class='line' id='LC48'><br/></div><div class='line' id='LC49'>	<span class="k">for</span> <span class="n">loc</span> <span class="ow">in</span> <span class="n">board</span><span class="o">.</span><span class="n">objects</span><span class="p">:</span></div><div class='line' id='LC50'>		<span class="k">if</span> <span class="n">board</span><span class="o">.</span><span class="n">get_object_at</span><span class="p">(</span><span class="n">loc</span><span class="p">)</span> <span class="o">==</span> <span class="n">board</span><span class="o">.</span><span class="n">PLAYER</span><span class="p">:</span></div><div class='line' id='LC51'>			<span class="n">player_loc</span> <span class="o">=</span> <span class="nb">eval</span><span class="p">(</span><span class="n">loc</span><span class="p">)</span></div><div class='line' id='LC52'>			<span class="n">player_locs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">player_loc</span><span class="p">)</span></div><div class='line' id='LC53'><br/></div><div class='line' id='LC54'>			<span class="n">player_dir</span> <span class="o">=</span> <span class="n">get_direction</span><span class="p">(</span><span class="n">player_loc</span><span class="p">)</span></div><div class='line' id='LC55'>			<span class="n">player_dist</span> <span class="o">=</span> <span class="n">get_distance</span><span class="p">(</span><span class="n">player_loc</span><span class="p">)</span></div><div class='line' id='LC56'>			<span class="n">player_slope</span> <span class="o">=</span> <span class="n">get_slope</span><span class="p">(</span><span class="n">player_loc</span><span class="p">)</span></div><div class='line' id='LC57'><br/></div><div class='line' id='LC58'><br/></div><div class='line' id='LC59'>			<span class="k">print</span> <span class="n">player_dist</span></div><div class='line' id='LC60'>			<span class="k">print</span> <span class="n">player_slope</span></div><div class='line' id='LC61'><br/></div><div class='line' id='LC62'>			<span class="k">if</span> <span class="n">player_dist</span> <span class="o">&lt;=</span> <span class="n">min_player_distance</span><span class="p">:</span></div><div class='line' id='LC63'>				<span class="n">possible_directions</span> <span class="o">=</span> <span class="n">get_possible_directions</span><span class="p">(</span><span class="n">get_opposite_diagonal_directions</span><span class="p">(</span><span class="n">player_dir</span><span class="p">)</span> <span class="p">,</span> <span class="n">Action</span><span class="o">.</span><span class="n">MOVE</span> <span class="p">,</span> <span class="n">order</span> <span class="o">=</span> <span class="mi">1</span> <span class="p">,</span> <span class="n">base</span> <span class="o">=</span> <span class="mi">15</span> <span class="o">*</span> <span class="n">math</span><span class="o">.</span><span class="n">pow</span><span class="p">(</span><span class="n">min_player_distance</span> <span class="o">-</span> <span class="n">player_dist</span> <span class="p">,</span> <span class="mi">2</span><span class="p">))</span></div><div class='line' id='LC64'>				<span class="n">possible_moves</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">possible_directions</span><span class="p">)</span></div><div class='line' id='LC65'>			<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC66'>				<span class="n">possible_directions</span> <span class="o">=</span> <span class="n">get_possible_directions</span><span class="p">([</span><span class="n">player_dir</span><span class="p">]</span> <span class="p">,</span> <span class="n">Action</span><span class="o">.</span><span class="n">MOVE</span> <span class="p">,</span> <span class="n">order</span> <span class="o">=</span> <span class="mi">2</span><span class="p">,</span> <span class="n">base</span> <span class="o">=</span> <span class="mi">8</span><span class="p">)</span></div><div class='line' id='LC67'>				<span class="n">possible_moves</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">possible_directions</span><span class="p">)</span></div><div class='line' id='LC68'><br/></div><div class='line' id='LC69'>			<span class="k">if</span> <span class="n">player_dist</span> <span class="o">&lt;=</span> <span class="n">max_throw_snowball_distance</span><span class="p">:</span></div><div class='line' id='LC70'>				<span class="n">possible_directions</span> <span class="o">=</span> <span class="n">get_possible_directions</span><span class="p">([</span><span class="n">player_dir</span><span class="p">]</span> <span class="p">,</span> <span class="n">Action</span><span class="o">.</span><span class="n">THROWSNOWBALL</span> <span class="p">,</span> <span class="n">order</span> <span class="o">=</span> <span class="mi">1</span> <span class="p">,</span> <span class="n">base</span> <span class="o">=</span> <span class="mi">20</span><span class="o">*</span><span class="p">(</span><span class="n">max_throw_snowball_distance</span> <span class="o">-</span> <span class="n">player_dist</span><span class="p">))</span></div><div class='line' id='LC71'>				<span class="n">possible_moves</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">possible_directions</span><span class="p">)</span></div><div class='line' id='LC72'><br/></div><div class='line' id='LC73'><br/></div><div class='line' id='LC74'>	<span class="c">#TODO: implement snowball tracking</span></div><div class='line' id='LC75'><br/></div><div class='line' id='LC76'>	<span class="n">tmp_snowball_locs</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span></div><div class='line' id='LC77'><br/></div><div class='line' id='LC78'>	<span class="k">for</span> <span class="p">(</span><span class="n">snowball_loc</span><span class="p">)</span> <span class="p">,</span> <span class="n">snowball_dir</span> <span class="ow">in</span> <span class="n">snowball_locs</span><span class="o">.</span><span class="n">iteritems</span><span class="p">():</span></div><div class='line' id='LC79'>		<span class="k">print</span> <span class="n">snowball_loc</span> <span class="p">,</span> <span class="n">snowball_dir</span></div><div class='line' id='LC80'>		<span class="n">snowball_loc</span> <span class="o">=</span> <span class="n">board</span><span class="o">.</span><span class="n">next_pos_in_direction</span><span class="p">(</span><span class="n">snowball_loc</span> <span class="p">,</span> <span class="n">snowball_dir</span><span class="p">,</span> <span class="n">amount</span> <span class="o">=</span> <span class="mi">2</span><span class="p">)</span></div><div class='line' id='LC81'>		<span class="k">if</span> <span class="n">board</span><span class="o">.</span><span class="n">get_object_at</span><span class="p">(</span><span class="n">snowball_loc</span><span class="p">)</span> <span class="o">==</span> <span class="n">board</span><span class="o">.</span><span class="n">SNOWBALL</span><span class="p">:</span></div><div class='line' id='LC82'>			<span class="n">tmp_snowball_locs</span><span class="p">[</span><span class="n">snowball_loc</span><span class="p">]</span> <span class="o">=</span> <span class="n">snowball_dir</span></div><div class='line' id='LC83'><br/></div><div class='line' id='LC84'>	<span class="n">snowball_locs</span> <span class="o">=</span> <span class="n">tmp_snowball_locs</span></div><div class='line' id='LC85'><br/></div><div class='line' id='LC86'>	<span class="c">#Fix this to deal with Rougue snowballs</span></div><div class='line' id='LC87'>	<span class="k">for</span> <span class="n">loc</span> <span class="ow">in</span> <span class="n">board</span><span class="o">.</span><span class="n">objects</span><span class="p">:</span></div><div class='line' id='LC88'>		<span class="k">if</span> <span class="n">board</span><span class="o">.</span><span class="n">get_object_at</span><span class="p">(</span><span class="n">loc</span><span class="p">)</span> <span class="o">==</span> <span class="n">board</span><span class="o">.</span><span class="n">SNOWBALL</span><span class="p">:</span></div><div class='line' id='LC89'>			<span class="n">snowball_loc</span> <span class="o">=</span> <span class="nb">eval</span><span class="p">(</span><span class="n">loc</span><span class="p">)</span></div><div class='line' id='LC90'>			<span class="k">if</span> <span class="n">snowball_loc</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">snowball_locs</span><span class="p">:</span></div><div class='line' id='LC91'>				<span class="n">min_player_dist</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">maxint</span></div><div class='line' id='LC92'>				<span class="n">closest_player_loc</span> <span class="o">=</span> <span class="p">()</span></div><div class='line' id='LC93'>				<span class="k">for</span> <span class="n">player_loc</span> <span class="ow">in</span> <span class="n">player_locs</span><span class="p">:</span></div><div class='line' id='LC94'>					<span class="n">player_dist</span> <span class="o">=</span> <span class="n">get_distance</span><span class="p">(</span><span class="n">snowball_loc</span> <span class="p">,</span> <span class="n">player_loc</span><span class="p">)</span></div><div class='line' id='LC95'>					<span class="k">if</span> <span class="n">player_dist</span> <span class="o">&lt;</span> <span class="n">min_player_dist</span><span class="p">:</span></div><div class='line' id='LC96'>						<span class="n">min_player_dist</span> <span class="o">=</span> <span class="n">player_dist</span></div><div class='line' id='LC97'>						<span class="n">closest_player_loc</span> <span class="o">=</span> <span class="n">player_loc</span></div><div class='line' id='LC98'>				<span class="n">snowball_dir</span> <span class="o">=</span> <span class="n">get_direction</span><span class="p">(</span><span class="n">snowball_loc</span> <span class="p">,</span> <span class="n">closest_player_loc</span><span class="p">)</span></div><div class='line' id='LC99'>				<span class="k">print</span> <span class="n">snowball_loc</span> <span class="p">,</span> <span class="n">snowball_dir</span></div><div class='line' id='LC100'>				<span class="n">snowball_locs</span><span class="p">[</span><span class="n">snowball_loc</span><span class="p">]</span> <span class="o">=</span> <span class="n">snowball_dir</span></div><div class='line' id='LC101'><br/></div><div class='line' id='LC102'><br/></div><div class='line' id='LC103'><br/></div><div class='line' id='LC104'>	<span class="n">avoid_locs</span> <span class="o">=</span> <span class="p">[]</span></div><div class='line' id='LC105'><br/></div><div class='line' id='LC106'>	<span class="c">#Fix this to something better once collision is understood</span></div><div class='line' id='LC107'>	<span class="k">for</span> <span class="p">(</span><span class="n">snowball_loc</span><span class="p">),</span> <span class="n">snowball_dir</span> <span class="ow">in</span> <span class="n">snowball_locs</span><span class="o">.</span><span class="n">iteritems</span><span class="p">():</span></div><div class='line' id='LC108'>		<span class="k">print</span> <span class="n">snowball_loc</span> <span class="p">,</span> <span class="n">snowball_dir</span></div><div class='line' id='LC109'>		<span class="n">avoid_locs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">snowball_loc</span><span class="p">)</span></div><div class='line' id='LC110'>		<span class="n">avoid_locs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">board</span><span class="o">.</span><span class="n">next_pos_in_direction</span><span class="p">(</span><span class="n">snowball_loc</span> <span class="p">,</span> <span class="n">snowball_dir</span><span class="p">))</span></div><div class='line' id='LC111'>		<span class="n">avoid_locs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">board</span><span class="o">.</span><span class="n">next_pos_in_direction</span><span class="p">(</span><span class="n">snowball_loc</span> <span class="p">,</span> <span class="n">snowball_dir</span><span class="p">,</span> <span class="n">amount</span> <span class="o">=</span> <span class="mi">2</span><span class="p">))</span></div><div class='line' id='LC112'><br/></div><div class='line' id='LC113'><br/></div><div class='line' id='LC114'>	<span class="n">possible_moves</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">get_possible_directions</span><span class="p">([</span><span class="n">curr_dir</span><span class="p">]</span> <span class="p">,</span> <span class="n">Action</span><span class="o">.</span><span class="n">MOVE</span> <span class="p">,</span> <span class="n">order</span> <span class="o">=</span> <span class="mi">4</span> <span class="p">,</span> <span class="n">base</span> <span class="o">=</span> <span class="mi">3</span><span class="p">))</span></div><div class='line' id='LC115'><br/></div><div class='line' id='LC116'>	<span class="k">print</span> <span class="n">possible_moves</span></div><div class='line' id='LC117'><br/></div><div class='line' id='LC118'>	<span class="n">possible_move</span> <span class="o">=</span> <span class="n">random</span><span class="o">.</span><span class="n">choice</span><span class="p">(</span><span class="n">possible_moves</span><span class="p">)</span></div><div class='line' id='LC119'><br/></div><div class='line' id='LC120'>	<span class="k">while</span> <span class="n">possible_move</span><span class="p">:</span></div><div class='line' id='LC121'>		<span class="n">possible_action</span> <span class="o">=</span> <span class="n">possible_move</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span></div><div class='line' id='LC122'>		<span class="n">possible_direction</span> <span class="o">=</span> <span class="n">possible_move</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span></div><div class='line' id='LC123'><br/></div><div class='line' id='LC124'>		<span class="k">if</span> <span class="n">possible_action</span> <span class="o">==</span> <span class="n">Action</span><span class="o">.</span><span class="n">MOVE</span><span class="p">:</span></div><div class='line' id='LC125'>			<span class="c">#Moving Action</span></div><div class='line' id='LC126'><br/></div><div class='line' id='LC127'>			<span class="c">#TODO Add all non-player pieces to avoid_locs</span></div><div class='line' id='LC128'>			<span class="n">possible_next_loc</span> <span class="o">=</span> <span class="n">board</span><span class="o">.</span><span class="n">next_pos_in_direction</span><span class="p">((</span><span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span> <span class="p">,</span> <span class="n">possible_direction</span><span class="p">)</span></div><div class='line' id='LC129'>			<span class="nb">object</span> <span class="o">=</span> <span class="n">board</span><span class="o">.</span><span class="n">get_object_at</span><span class="p">(</span><span class="n">possible_next_loc</span><span class="p">)</span></div><div class='line' id='LC130'>			<span class="k">if</span> <span class="nb">object</span> <span class="ow">or</span> <span class="n">possible_next_loc</span> <span class="ow">in</span> <span class="n">avoid_locs</span><span class="p">:</span></div><div class='line' id='LC131'>				<span class="n">possible_move</span> <span class="o">=</span> <span class="n">random</span><span class="o">.</span><span class="n">choice</span><span class="p">(</span><span class="n">possible_moves</span><span class="p">)</span></div><div class='line' id='LC132'>				<span class="k">continue</span></div><div class='line' id='LC133'>			<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC134'>				<span class="n">curr_dir</span> <span class="o">=</span> <span class="n">possible_direction</span></div><div class='line' id='LC135'><br/></div><div class='line' id='LC136'>				<span class="k">for</span> <span class="n">snowball_loc</span><span class="p">,</span> <span class="n">snowball_dir</span> <span class="ow">in</span> <span class="n">snowball_locs</span><span class="o">.</span><span class="n">iteritems</span><span class="p">():</span></div><div class='line' id='LC137'>					<span class="n">snowball_loc</span> <span class="o">=</span> <span class="n">get_next_pos_in_direction</span><span class="p">(</span><span class="n">snowball_loc</span> <span class="p">,</span> <span class="n">get_opposite_direction</span><span class="p">(</span><span class="n">curr_dir</span><span class="p">))</span></div><div class='line' id='LC138'><br/></div><div class='line' id='LC139'>				<span class="k">return</span> <span class="n">possible_move</span></div><div class='line' id='LC140'>		<span class="k">elif</span> <span class="n">possible_action</span> <span class="o">==</span> <span class="n">Action</span><span class="o">.</span><span class="n">THROWSNOWBALL</span><span class="p">:</span></div><div class='line' id='LC141'>			<span class="k">if</span> <span class="n">snowballs</span> <span class="o">&gt;</span> <span class="mi">0</span> <span class="ow">and</span> <span class="n">curr_loc</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">avoid_locs</span><span class="p">:</span></div><div class='line' id='LC142'>				<span class="k">print</span> <span class="s">"Throwing Snowball"</span><span class="p">,</span> <span class="n">possible_direction</span></div><div class='line' id='LC143'>				<span class="n">curr_dir</span> <span class="o">=</span> <span class="n">possible_direction</span></div><div class='line' id='LC144'>				<span class="k">print</span> <span class="n">curr_loc</span> <span class="p">,</span> <span class="n">curr_dir</span></div><div class='line' id='LC145'>				<span class="n">snowball_locs</span><span class="p">[</span><span class="n">curr_loc</span><span class="p">]</span> <span class="o">=</span> <span class="n">curr_dir</span>		</div><div class='line' id='LC146'>				<span class="n">snowballs</span> <span class="o">-=</span> <span class="mi">1</span></div><div class='line' id='LC147'>				<span class="k">return</span> <span class="n">possible_move</span></div><div class='line' id='LC148'>			<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC149'>				<span class="n">possible_move</span> <span class="o">=</span> <span class="n">random</span><span class="o">.</span><span class="n">choice</span><span class="p">(</span><span class="n">possible_moves</span><span class="p">)</span></div><div class='line' id='LC150'>		<span class="k">elif</span> <span class="n">possible_action</span> <span class="o">==</span> <span class="n">Action</span><span class="o">.</span><span class="n">MAKESNOWBALL</span><span class="p">:</span></div><div class='line' id='LC151'>			<span class="k">if</span> <span class="n">curr_loc</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">avoid_locs</span><span class="p">:</span></div><div class='line' id='LC152'>				<span class="n">curr_dir</span> <span class="o">=</span> <span class="n">possible_direction</span></div><div class='line' id='LC153'>				<span class="n">snowballs</span> <span class="o">+=</span> <span class="mi">1</span></div><div class='line' id='LC154'>				<span class="k">return</span> <span class="n">possible_move</span></div><div class='line' id='LC155'>			<span class="k">else</span><span class="p">:</span> </div><div class='line' id='LC156'>				<span class="n">possible_move</span> <span class="o">=</span> <span class="n">random</span><span class="o">.</span><span class="n">choice</span><span class="p">(</span><span class="n">possible_moves</span><span class="p">)</span></div><div class='line' id='LC157'><br/></div><div class='line' id='LC158'><br/></div><div class='line' id='LC159'><span class="k">def</span> <span class="nf">get_distance</span><span class="p">(</span><span class="n">loc</span> <span class="p">,</span> <span class="n">curr_loc</span><span class="o">=</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">)):</span></div><div class='line' id='LC160'>	<span class="k">return</span> <span class="n">math</span><span class="o">.</span><span class="n">sqrt</span><span class="p">(</span><span class="n">math</span><span class="o">.</span><span class="n">pow</span><span class="p">(</span><span class="n">loc</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">-</span> <span class="n">curr_loc</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="p">,</span> <span class="mi">2</span><span class="p">)</span> <span class="o">+</span> <span class="n">math</span><span class="o">.</span><span class="n">pow</span><span class="p">(</span><span class="n">loc</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="o">-</span> <span class="n">curr_loc</span><span class="p">[</span><span class="mi">1</span><span class="p">],</span> <span class="mi">2</span><span class="p">))</span></div><div class='line' id='LC161'><br/></div><div class='line' id='LC162'><span class="k">def</span> <span class="nf">get_direction</span><span class="p">(</span><span class="n">loc</span> <span class="p">,</span> <span class="n">curr_loc</span><span class="o">=</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">)):</span></div><div class='line' id='LC163'>	<span class="c">#global last_loc</span></div><div class='line' id='LC164'><br/></div><div class='line' id='LC165'>	<span class="n">x_diff</span> <span class="o">=</span> <span class="n">curr_loc</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">-</span> <span class="n">loc</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span></div><div class='line' id='LC166'>	<span class="n">y_diff</span> <span class="o">=</span> <span class="n">curr_loc</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="o">-</span> <span class="n">loc</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span></div><div class='line' id='LC167'><br/></div><div class='line' id='LC168'>	<span class="k">if</span> <span class="n">x_diff</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span></div><div class='line' id='LC169'>		<span class="c">#Some kind of west</span></div><div class='line' id='LC170'>		<span class="k">if</span> <span class="n">y_diff</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="p">:</span></div><div class='line' id='LC171'>			<span class="k">return</span> <span class="n">Direction</span><span class="o">.</span><span class="n">SOUTHWEST</span></div><div class='line' id='LC172'>		<span class="k">elif</span> <span class="n">y_diff</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span></div><div class='line' id='LC173'>			<span class="k">return</span> <span class="n">Direction</span><span class="o">.</span><span class="n">NORTHWEST</span></div><div class='line' id='LC174'>		<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC175'>			<span class="k">return</span> <span class="n">Direction</span><span class="o">.</span><span class="n">WEST</span></div><div class='line' id='LC176'>	<span class="k">elif</span> <span class="n">x_diff</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="p">:</span></div><div class='line' id='LC177'>		<span class="c">#Some kind of east</span></div><div class='line' id='LC178'>		<span class="k">if</span> <span class="n">y_diff</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="p">:</span></div><div class='line' id='LC179'>			<span class="k">return</span> <span class="n">Direction</span><span class="o">.</span><span class="n">SOUTHEAST</span></div><div class='line' id='LC180'>		<span class="k">elif</span> <span class="n">y_diff</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span> </div><div class='line' id='LC181'>			<span class="k">return</span> <span class="n">Direction</span><span class="o">.</span><span class="n">NORTHEAST</span></div><div class='line' id='LC182'>		<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC183'>			<span class="k">return</span> <span class="n">Direction</span><span class="o">.</span><span class="n">EAST</span></div><div class='line' id='LC184'>	<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC185'>		<span class="k">if</span> <span class="n">y_diff</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span></div><div class='line' id='LC186'>			<span class="k">return</span> <span class="n">Direction</span><span class="o">.</span><span class="n">NORTH</span></div><div class='line' id='LC187'>		<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC188'>			<span class="k">return</span> <span class="n">Direction</span><span class="o">.</span><span class="n">SOUTH</span> </div><div class='line' id='LC189'><br/></div><div class='line' id='LC190'><span class="k">def</span> <span class="nf">get_slope</span><span class="p">(</span><span class="n">loc</span> <span class="p">,</span> <span class="n">curr_loc</span> <span class="o">=</span> <span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">)):</span></div><div class='line' id='LC191'>	<span class="k">if</span> <span class="n">curr_loc</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="o">-</span> <span class="n">loc</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span></div><div class='line' id='LC192'>		<span class="k">return</span> <span class="mi">0</span></div><div class='line' id='LC193'>	<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC194'>		<span class="k">return</span> <span class="nb">float</span><span class="p">((</span><span class="n">curr_loc</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">-</span> <span class="n">loc</span><span class="p">[</span><span class="mi">0</span><span class="p">]))</span> <span class="o">/</span> <span class="nb">float</span><span class="p">((</span><span class="n">curr_loc</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="o">-</span> <span class="n">loc</span><span class="p">[</span><span class="mi">1</span><span class="p">]))</span></div><div class='line' id='LC195'><br/></div><div class='line' id='LC196'><span class="k">def</span> <span class="nf">get_opposite_direction</span><span class="p">(</span><span class="n">direction</span><span class="p">):</span></div><div class='line' id='LC197'>	<span class="k">return</span> <span class="p">(</span><span class="n">direction</span> <span class="o">+</span> <span class="mi">4</span><span class="p">)</span> <span class="o">%</span> <span class="mi">8</span></div><div class='line' id='LC198'><br/></div><div class='line' id='LC199'><span class="k">def</span> <span class="nf">get_opposite_diagonal_directions</span><span class="p">(</span><span class="n">direction</span><span class="p">):</span></div><div class='line' id='LC200'>	<span class="k">return</span> <span class="p">[(</span><span class="n">direction</span> <span class="o">+</span> <span class="mi">3</span> <span class="p">)</span> <span class="o">%</span> <span class="mi">8</span> <span class="p">,</span> <span class="p">(</span><span class="n">direction</span> <span class="o">+</span> <span class="mi">5</span><span class="p">)</span> <span class="o">%</span> <span class="mi">8</span><span class="p">]</span></div><div class='line' id='LC201'><br/></div><div class='line' id='LC202'><span class="k">def</span> <span class="nf">get_perp_directions</span><span class="p">(</span><span class="n">direction</span><span class="p">):</span></div><div class='line' id='LC203'>	<span class="k">return</span> <span class="p">(</span><span class="n">direction</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span> <span class="o">%</span> <span class="mi">8</span></div><div class='line' id='LC204'><br/></div><div class='line' id='LC205'><span class="k">def</span> <span class="nf">get_possible_directions</span><span class="p">(</span><span class="n">directions</span> <span class="p">,</span> <span class="n">action</span><span class="p">,</span>  <span class="n">order</span> <span class="o">=</span> <span class="mi">2</span> <span class="p">,</span> <span class="n">base</span> <span class="o">=</span> <span class="mi">2</span><span class="p">):</span></div><div class='line' id='LC206'>	<span class="n">possible_directions</span> <span class="o">=</span> <span class="nb">list</span><span class="p">()</span> </div><div class='line' id='LC207'>	<span class="k">for</span> <span class="n">direction</span> <span class="ow">in</span> <span class="n">directions</span><span class="p">:</span></div><div class='line' id='LC208'>		<span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">order</span> <span class="o">*</span> <span class="o">-</span><span class="mi">1</span> <span class="p">,</span> <span class="n">order</span><span class="p">):</span></div><div class='line' id='LC209'>			<span class="c">#print i , direction</span></div><div class='line' id='LC210'>			<span class="n">possible_direction</span> <span class="o">=</span> <span class="p">(</span><span class="n">direction</span> <span class="o">+</span> <span class="n">i</span> <span class="o">+</span> <span class="mi">8</span><span class="p">)</span> <span class="o">%</span> <span class="mi">8</span></div><div class='line' id='LC211'>			<span class="n">possible_order</span> <span class="o">=</span> <span class="n">math</span><span class="o">.</span><span class="n">pow</span><span class="p">(</span><span class="n">base</span> <span class="p">,</span> <span class="n">order</span> <span class="o">-</span> <span class="nb">abs</span><span class="p">(</span><span class="n">i</span><span class="p">))</span></div><div class='line' id='LC212'><br/></div><div class='line' id='LC213'>			<span class="c">#print possible_direction , possible_order</span></div><div class='line' id='LC214'><br/></div><div class='line' id='LC215'>			<span class="n">possible_direction_tuple</span> <span class="o">=</span> <span class="p">(</span><span class="n">action</span> <span class="p">,</span> <span class="n">possible_direction</span><span class="p">)</span></div><div class='line' id='LC216'><br/></div><div class='line' id='LC217'>			<span class="n">curr_order</span> <span class="o">=</span> <span class="n">possible_directions</span><span class="o">.</span><span class="n">count</span><span class="p">(</span><span class="n">possible_direction_tuple</span><span class="p">)</span></div><div class='line' id='LC218'><br/></div><div class='line' id='LC219'>			<span class="k">if</span> <span class="n">possible_order</span> <span class="o">&gt;</span> <span class="n">curr_order</span><span class="p">:</span></div><div class='line' id='LC220'>				<span class="n">possible_order</span> <span class="o">=</span> <span class="n">possible_order</span> <span class="o">-</span> <span class="n">curr_order</span></div><div class='line' id='LC221'>				<span class="k">for</span> <span class="n">j</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">possible_order</span><span class="p">):</span></div><div class='line' id='LC222'>					<span class="c">#print possible_direction_tuple</span></div><div class='line' id='LC223'>					<span class="n">possible_directions</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">possible_direction_tuple</span><span class="p">)</span></div><div class='line' id='LC224'>	<span class="k">return</span> <span class="n">possible_directions</span></div><div class='line' id='LC225'><br/></div><div class='line' id='LC226'><span class="c"># Initial direction to try to move</span></div><div class='line' id='LC227'><span class="n">curr_dir</span> <span class="o">=</span> <span class="n">Direction</span><span class="o">.</span><span class="n">SOUTH</span></div><div class='line' id='LC228'><span class="n">curr_loc</span> <span class="o">=</span> <span class="p">(</span><span class="mi">0</span> <span class="p">,</span> <span class="mi">0</span><span class="p">)</span></div><div class='line' id='LC229'><span class="n">snowball_locs</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span></div><div class='line' id='LC230'><br/></div><div class='line' id='LC231'><span class="n">snowballs</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC232'><span class="n">snowball_target</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC233'><span class="n">min_snowballs</span> <span class="o">=</span> <span class="mi">3</span></div><div class='line' id='LC234'><span class="n">max_snowballs</span> <span class="o">=</span> <span class="mi">10</span></div><div class='line' id='LC235'><br/></div><div class='line' id='LC236'><span class="n">min_player_distance</span> <span class="o">=</span> <span class="mf">3.5</span></div><div class='line' id='LC237'><br/></div><div class='line' id='LC238'><span class="n">max_throw_snowball_distance</span> <span class="o">=</span> <span class="mi">7</span></div><div class='line' id='LC239'><br/></div><div class='line' id='LC240'><br/></div><div class='line' id='LC241'><span class="c"># Create our client</span></div><div class='line' id='LC242'><span class="n">c</span> <span class="o">=</span> <span class="n">Client</span><span class="p">()</span></div><div class='line' id='LC243'><br/></div><div class='line' id='LC244'><span class="c"># Insert your key here</span></div><div class='line' id='LC245'><span class="n">c</span><span class="o">.</span><span class="n">KEY</span> <span class="o">=</span> <span class="s">"g2lVRjJN96svcwTYPG8K0MmUfdQq6Xg1"</span> </div><div class='line' id='LC246'><br/></div><div class='line' id='LC247'><br/></div><div class='line' id='LC248'><span class="c"># Tell the client to use this function to decide the next move.</span></div><div class='line' id='LC249'><span class="c"># This function is defined above.</span></div><div class='line' id='LC250'><span class="n">c</span><span class="o">.</span><span class="n">decide_move</span> <span class="o">=</span> <span class="n">dummy</span></div><div class='line' id='LC251'><br/></div><div class='line' id='LC252'><span class="c"># Connect to the game server</span></div><div class='line' id='LC253'><span class="k">if</span> <span class="n">c</span><span class="o">.</span><span class="n">connect</span><span class="p">():</span></div><div class='line' id='LC254'>	<span class="c"># If we successfully connected, start playing</span></div><div class='line' id='LC255'>	<span class="k">print</span> <span class="s">&#39;Connected&#39;</span></div><div class='line' id='LC256'><br/></div><div class='line' id='LC257'>	<span class="c"># Tell the client to start listening for maps</span></div><div class='line' id='LC258'>	<span class="n">c</span><span class="o">.</span><span class="n">start</span><span class="p">()</span></div><div class='line' id='LC259'><br/></div><div class='line' id='LC260'>	<span class="c"># Wait until the user presses a key</span></div><div class='line' id='LC261'>	<span class="nb">raw_input</span><span class="p">(</span><span class="s">&#39;Press any key to quit...&#39;</span><span class="p">)</span></div><div class='line' id='LC262'><br/></div><div class='line' id='LC263'>	<span class="c"># Tell the client to stop listening for maps</span></div><div class='line' id='LC264'>	<span class="n">c</span><span class="o">.</span><span class="n">stop</span><span class="p">()</span></div><div class='line' id='LC265'><br/></div><div class='line' id='LC266'>	<span class="c"># Wait for the client to finish its last request</span></div><div class='line' id='LC267'>	<span class="n">c</span><span class="o">.</span><span class="n">join</span><span class="p">()</span></div><div class='line' id='LC268'><br/></div><div class='line' id='LC269'>	<span class="c"># Disconnect from the server</span></div><div class='line' id='LC270'>	<span class="n">c</span><span class="o">.</span><span class="n">disconnect</span><span class="p">()</span></div><div class='line' id='LC271'><span class="k">else</span><span class="p">:</span></div><div class='line' id='LC272'>	<span class="c"># If we didn&#39;t successfully connected, exit</span></div><div class='line' id='LC273'>	<span class="k">print</span> <span class="s">&#39;Could not connect&#39;</span></div><div class='line' id='LC274'><br/></div></pre></div>
              
            
          </td>
        </tr>
      </table>
    
  </div>


      </div>
    </div>
  


    </div>
  
      
    </div>

    <div id="footer" class="clearfix">
      <div class="site">
        <div class="sponsor">
          <a href="http://www.rackspace.com" class="logo">
            <img alt="Dedicated Server" src="https://assets0.github.com/images/modules/footer/rackspace_logo.png?v2?94b2d09e9a7ab2667d0731c6255d63c907ac01a5" />
          </a>
          Powered by the <a href="http://www.rackspace.com ">Dedicated
          Servers</a> and<br/> <a href="http://www.rackspacecloud.com">Cloud
          Computing</a> of Rackspace Hosting<span>&reg;</span>
        </div>

        <ul class="links">
          <li class="blog"><a href="https://github.com/blog">Blog</a></li>
          <li><a href="http://support.github.com">Support</a></li>
          <li><a href="https://github.com/training">Training</a></li>
          <li><a href="http://jobs.github.com">Job Board</a></li>
          <li><a href="http://shop.github.com">Shop</a></li>
          <li><a href="https://github.com/contact">Contact</a></li>
          <li><a href="http://develop.github.com">API</a></li>
          <li><a href="http://status.github.com">Status</a></li>
        </ul>
        <ul class="sosueme">
          <li class="main">&copy; 2010 <span id="_rrt" title="0.36858s from fe3.rs.github.com">GitHub</span> Inc. All rights reserved.</li>
          <li><a href="/site/terms">Terms of Service</a></li>
          <li><a href="/site/privacy">Privacy</a></li>
          <li><a href="https://github.com/security">Security</a></li>
        </ul>
      </div>
    </div><!-- /#footer -->

    
      
      
        <!-- current locale:  -->
        <div class="locales">
          <div class="site">

            <ul class="choices clearfix limited-locales">
              <li><span class="current">English</span></li>
              
                  <li><a rel="nofollow" href="?locale=de">Deutsch</a></li>
              
                  <li><a rel="nofollow" href="?locale=fr">Français</a></li>
              
                  <li><a rel="nofollow" href="?locale=ja">日本語</a></li>
              
                  <li><a rel="nofollow" href="?locale=pt-BR">Português (BR)</a></li>
              
                  <li><a rel="nofollow" href="?locale=ru">Русский</a></li>
              
                  <li><a rel="nofollow" href="?locale=zh">中文</a></li>
              
              <li class="all"><a href="#" class="minibutton btn-forward js-all-locales"><span><span class="icon"></span>See all available languages</span></a></li>
            </ul>

            <div class="all-locales clearfix">
              <h3>Your current locale selection: <strong>English</strong>. Choose another?</h3>
              
              
                <ul class="choices">
                  
                      <li><a rel="nofollow" href="?locale=en">English</a></li>
                  
                      <li><a rel="nofollow" href="?locale=af">Afrikaans</a></li>
                  
                      <li><a rel="nofollow" href="?locale=ca">Català</a></li>
                  
                      <li><a rel="nofollow" href="?locale=cs">Čeština</a></li>
                  
                </ul>
              
                <ul class="choices">
                  
                      <li><a rel="nofollow" href="?locale=de">Deutsch</a></li>
                  
                      <li><a rel="nofollow" href="?locale=es">Español</a></li>
                  
                      <li><a rel="nofollow" href="?locale=fr">Français</a></li>
                  
                      <li><a rel="nofollow" href="?locale=hr">Hrvatski</a></li>
                  
                </ul>
              
                <ul class="choices">
                  
                      <li><a rel="nofollow" href="?locale=id">Indonesia</a></li>
                  
                      <li><a rel="nofollow" href="?locale=it">Italiano</a></li>
                  
                      <li><a rel="nofollow" href="?locale=ja">日本語</a></li>
                  
                      <li><a rel="nofollow" href="?locale=nl">Nederlands</a></li>
                  
                </ul>
              
                <ul class="choices">
                  
                      <li><a rel="nofollow" href="?locale=no">Norsk</a></li>
                  
                      <li><a rel="nofollow" href="?locale=pl">Polski</a></li>
                  
                      <li><a rel="nofollow" href="?locale=pt-BR">Português (BR)</a></li>
                  
                      <li><a rel="nofollow" href="?locale=ru">Русский</a></li>
                  
                </ul>
              
                <ul class="choices">
                  
                      <li><a rel="nofollow" href="?locale=sr">Српски</a></li>
                  
                      <li><a rel="nofollow" href="?locale=sv">Svenska</a></li>
                  
                      <li><a rel="nofollow" href="?locale=zh">中文</a></li>
                  
                </ul>
              
            </div>

          </div>
          <div class="fade"></div>
        </div>
      
    

    <script>window._auth_token = "c7d1cd86b87e139668d9306efe0c18637dae9447"</script>
    <div id="keyboard_shortcuts_pane" style="display:none">
  <h2>Keyboard Shortcuts</h2>

  <div class="columns threecols">
    <div class="column first">
      <h3>Site wide shortcuts</h3>
      <dl class="keyboard-mappings">
        <dt>s</dt>
        <dd>Focus site search</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>?</dt>
        <dd>Bring up this help dialog</dd>
      </dl>
    </div><!-- /.column.first -->
    <div class="column middle">
      <h3>Commit list</h3>
      <dl class="keyboard-mappings">
        <dt>j</dt>
        <dd>Move selected down</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>k</dt>
        <dd>Move selected up</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>t</dt>
        <dd>Open tree</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>p</dt>
        <dd>Open parent</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>c <em>or</em> o <em>or</em> enter</dt>
        <dd>Open commit</dd>
      </dl>
    </div><!-- /.column.first -->
    <div class="column last">
      <h3>Pull request list</h3>
      <dl class="keyboard-mappings">
        <dt>j</dt>
        <dd>Move selected down</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>k</dt>
        <dd>Move selected up</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>o <em>or</em> enter</dt>
        <dd>Open issue</dd>
      </dl>
    </div><!-- /.columns.last -->
  </div><!-- /.columns.equacols -->

  <div class="rule"></div>

  <h3>Issues</h3>

  <div class="columns threecols">
    <div class="column first">
      <dl class="keyboard-mappings">
        <dt>j</dt>
        <dd>Move selected down</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>k</dt>
        <dd>Move selected up</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>x</dt>
        <dd>Toggle select target</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>o <em>or</em> enter</dt>
        <dd>Open issue</dd>
      </dl>
    </div><!-- /.column.first -->
    <div class="column middle">
      <dl class="keyboard-mappings">
        <dt>I</dt>
        <dd>Mark selected as read</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>U</dt>
        <dd>Mark selected as unread</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>e</dt>
        <dd>Close selected</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>y</dt>
        <dd>Remove selected from view</dd>
      </dl>
    </div><!-- /.column.middle -->
    <div class="column last">
      <dl class="keyboard-mappings">
        <dt>c</dt>
        <dd>Create issue</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>l</dt>
        <dd>Create label</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>i</dt>
        <dd>Back to inbox</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>u</dt>
        <dd>Back to issues</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>/</dt>
        <dd>Focus issues search</dd>
      </dl>
    </div>
  </div>

  <div class="rule"></div>

  <h3>Network Graph</h3>
  <div class="columns equacols">
    <div class="column first">
      <dl class="keyboard-mappings">
        <dt>← <em>or</em> h</dt>
        <dd>Scroll left</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>→ <em>or</em> l</dt>
        <dd>Scroll right</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>↑ <em>or</em> k</dt>
        <dd>Scroll up</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>↓ <em>or</em> j</dt>
        <dd>Scroll down</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>t</dt>
        <dd>Toggle visibility of head labels</dd>
      </dl>
    </div><!-- /.column.first -->
    <div class="column last">
      <dl class="keyboard-mappings">
        <dt>shift ← <em>or</em> shift h</dt>
        <dd>Scroll all the way left</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>shift → <em>or</em> shift l</dt>
        <dd>Scroll all the way right</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>shift ↑ <em>or</em> shift k</dt>
        <dd>Scroll all the way up</dd>
      </dl>
      <dl class="keyboard-mappings">
        <dt>shift ↓ <em>or</em> shift j</dt>
        <dd>Scroll all the way down</dd>
      </dl>
    </div><!-- /.column.last -->
  </div>

</div>
    

    <!--[if IE 8]>
    <script type="text/javascript" charset="utf-8">
      $(document.body).addClass("ie8")
    </script>
    <![endif]-->

    <!--[if IE 7]>
    <script type="text/javascript" charset="utf-8">
      $(document.body).addClass("ie7")
    </script>
    <![endif]-->

    <script type="text/javascript">
      _kmq.push(['trackClick', 'entice-signup-button', 'Entice banner clicked']);
      
    </script>
    
  </body>
</html>

