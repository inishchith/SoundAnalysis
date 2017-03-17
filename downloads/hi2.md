





<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">



  <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/frameworks-a4f2fd2194ac92143e2698e03e7a16834295fcca38543fc5737201884315ebe9.css" media="all" rel="stylesheet" />
  <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/github-a20b0761ae9a52b4ed0d75922904eb8ffb5934a855914ec141ff3b2140a18b9a.css" media="all" rel="stylesheet" />
  
  
  <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/site-b29e324b8fafaead965049ef224818ef0dccc7384b5cfcad56a56a89c33a9438.css" media="all" rel="stylesheet" />
  

  <meta name="viewport" content="width=device-width">
  
  <title>learnxinyminutes-docs/CHICKEN.html.markdown at master · adambard/learnxinyminutes-docs · GitHub</title>
  <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
  <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
  <meta property="fb:app_id" content="1401488693436528">

    
    <meta content="https://avatars2.githubusercontent.com/u/515720?v=3&amp;s=400" property="og:image" /><meta content="GitHub" property="og:site_name" /><meta content="object" property="og:type" /><meta content="adambard/learnxinyminutes-docs" property="og:title" /><meta content="https://github.com/adambard/learnxinyminutes-docs" property="og:url" /><meta content="learnxinyminutes-docs - Code documentation written as code! How novel and totally my idea!" property="og:description" />

  <link rel="assets" href="https://assets-cdn.github.com/">
  
  <meta name="pjax-timeout" content="1000">
  
  <meta name="request-id" content="C9D1:125D:50A3DB:7D1783:58CB5686" data-pjax-transient>
  

  <meta name="selected-link" value="repo_source" data-pjax-transient>

  <meta name="google-site-verification" content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU">
<meta name="google-site-verification" content="ZzhVyEFwb7w3e0-uOTltm8Jsck2F5StVihD0exw2fsA">
    <meta name="google-analytics" content="UA-3769691-2">

<meta content="collector.githubapp.com" name="octolytics-host" /><meta content="github" name="octolytics-app-id" /><meta content="https://collector.githubapp.com/github-external/browser_event" name="octolytics-event-url" /><meta content="C9D1:125D:50A3DB:7D1783:58CB5686" name="octolytics-dimension-request_id" />
<meta content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-pjax-transient="true" name="analytics-location" />




  <meta class="js-ga-set" name="dimension1" content="Logged Out">


  
  
      <meta name="hostname" content="github.com">
  <meta name="user-login" content="">

      <meta name="expected-hostname" content="github.com">
    <meta name="js-proxy-site-detection-payload" content="ZTA0MWYwZDNmY2JiOWNlYWVmMTAxODI3YTQwMmUzMWE4NGRjMGQ2OTZmNjBjMDhiOGY1Y2NhNjcxNGM3MmYwY3x7InJlbW90ZV9hZGRyZXNzIjoiMjIzLjIyOS4yMDAuMjQ4IiwicmVxdWVzdF9pZCI6IkM5RDE6MTI1RDo1MEEzREI6N0QxNzgzOjU4Q0I1Njg2IiwidGltZXN0YW1wIjoxNDg5NzIwOTY3LCJob3N0IjoiZ2l0aHViLmNvbSJ9">


  <meta name="html-safe-nonce" content="6187b97ffe6e8003fd0e82202a46db57dbe7ff65">

  <meta http-equiv="x-pjax-version" content="f365064fc2e31ed8d0a54eb155ce48ea">
  

    
  <meta name="description" content="learnxinyminutes-docs - Code documentation written as code! How novel and totally my idea!">
  <meta name="go-import" content="github.com/adambard/learnxinyminutes-docs git https://github.com/adambard/learnxinyminutes-docs.git">

  <meta content="515720" name="octolytics-dimension-user_id" /><meta content="adambard" name="octolytics-dimension-user_login" /><meta content="10974951" name="octolytics-dimension-repository_id" /><meta content="adambard/learnxinyminutes-docs" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="10974951" name="octolytics-dimension-repository_network_root_id" /><meta content="adambard/learnxinyminutes-docs" name="octolytics-dimension-repository_network_root_nwo" />
      <link href="https://github.com/adambard/learnxinyminutes-docs/commits/master.atom" rel="alternate" title="Recent Commits to learnxinyminutes-docs:master" type="application/atom+xml">


    <link rel="canonical" href="https://github.com/adambard/learnxinyminutes-docs/blob/master/CHICKEN.html.markdown" data-pjax-transient>


  <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">

  <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">

  <link rel="mask-icon" href="https://assets-cdn.github.com/pinned-octocat.svg" color="#000000">
  <link rel="icon" type="image/x-icon" href="https://assets-cdn.github.com/favicon.ico">

<meta name="theme-color" content="#1e2327">



  </head>

  <body class="logged-out env-production page-blob">
    

  <div class="position-relative js-header-wrapper ">
    <a href="#start-of-content" tabindex="1" class="accessibility-aid js-skip-to-content">Skip to content</a>
    <div id="js-pjax-loader-bar" class="pjax-loader-bar"><div class="progress"></div></div>

    
    
    



          <header class="site-header js-details-container Details" role="banner">
  <div class="container-responsive">
    <a class="header-logo-invertocat" href="https://github.com/" aria-label="Homepage" data-ga-click="(Logged out) Header, go to homepage, icon:logo-wordmark">
      <svg aria-hidden="true" class="octicon octicon-mark-github" height="32" version="1.1" viewBox="0 0 16 16" width="32"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
    </a>

    <button class="btn-link float-right site-header-toggle js-details-target" type="button" aria-label="Toggle navigation">
      <svg aria-hidden="true" class="octicon octicon-three-bars" height="24" version="1.1" viewBox="0 0 12 16" width="18"><path fill-rule="evenodd" d="M11.41 9H.59C0 9 0 8.59 0 8c0-.59 0-1 .59-1H11.4c.59 0 .59.41.59 1 0 .59 0 1-.59 1h.01zm0-4H.59C0 5 0 4.59 0 4c0-.59 0-1 .59-1H11.4c.59 0 .59.41.59 1 0 .59 0 1-.59 1h.01zM.59 11H11.4c.59 0 .59.41.59 1 0 .59 0 1-.59 1H.59C0 13 0 12.59 0 12c0-.59 0-1 .59-1z"/></svg>
    </button>

    <div class="site-header-menu">
      <nav class="site-header-nav">
        <a href="/features" class="js-selected-navigation-item nav-item" data-ga-click="Header, click, Nav menu - item:features" data-selected-links="/features /features">
          Features
</a>        <a href="/explore" class="js-selected-navigation-item nav-item" data-ga-click="Header, click, Nav menu - item:explore" data-selected-links="/explore /trending /trending/developers /integrations /integrations/feature/code /integrations/feature/collaborate /integrations/feature/ship /showcases /explore">
          Explore
</a>        <a href="/pricing" class="js-selected-navigation-item nav-item" data-ga-click="Header, click, Nav menu - item:pricing" data-selected-links="/pricing /pricing">
          Pricing
</a>      </nav>

      <div class="site-header-actions">
          <div class="header-search scoped-search site-scoped-search js-site-search" role="search">
  <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/adambard/learnxinyminutes-docs/search" class="js-site-search-form" data-scoped-search-url="/adambard/learnxinyminutes-docs/search" data-unscoped-search-url="/search" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
    <label class="form-control header-search-wrapper js-chromeless-input-container">
      <div class="header-search-scope">This repository</div>
      <input type="text"
        class="form-control header-search-input js-site-search-focus js-site-search-field is-clearable"
        data-hotkey="s"
        name="q"
        placeholder="Search"
        aria-label="Search this repository"
        data-unscoped-placeholder="Search GitHub"
        data-scoped-placeholder="Search"
        autocapitalize="off">
    </label>
</form></div>


          <a class="text-bold site-header-link" href="/login?return_to=%2Fadambard%2Flearnxinyminutes-docs%2Fblob%2Fmaster%2FCHICKEN.html.markdown" data-ga-click="(Logged out) Header, clicked Sign in, text:sign-in">Sign in</a>
            <span class="text-gray">or</span>
            <a class="text-bold site-header-link" href="/join?source=header-repo" data-ga-click="(Logged out) Header, clicked Sign up, text:sign-up">Sign up</a>
      </div>
    </div>
  </div>
</header>


  </div>

  <div id="start-of-content" class="accessibility-aid"></div>

    <div id="js-flash-container">
</div>



  <div role="main">
      <div itemscope itemtype="http://schema.org/SoftwareSourceCode">
    <div id="js-repo-pjax-container" data-pjax-container>
        


<div class="pagehead repohead instapaper_ignore readability-menu experiment-repo-nav">
  <div class="container repohead-details-container">


    <ul class="pagehead-actions">
  <li>
      <a href="/login?return_to=%2Fadambard%2Flearnxinyminutes-docs"
    class="btn btn-sm btn-with-count tooltipped tooltipped-n"
    aria-label="You must be signed in to watch a repository" rel="nofollow">
    <svg aria-hidden="true" class="octicon octicon-eye" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
    Watch
  </a>
  <a class="social-count" href="/adambard/learnxinyminutes-docs/watchers"
     aria-label="163 users are watching this repository">
    163
  </a>

  </li>

  <li>
      <a href="/login?return_to=%2Fadambard%2Flearnxinyminutes-docs"
    class="btn btn-sm btn-with-count tooltipped tooltipped-n"
    aria-label="You must be signed in to star a repository" rel="nofollow">
    <svg aria-hidden="true" class="octicon octicon-star" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74z"/></svg>
    Star
  </a>

    <a class="social-count js-social-count" href="/adambard/learnxinyminutes-docs/stargazers"
      aria-label="4310 users starred this repository">
      4,310
    </a>

  </li>

  <li>
      <a href="/login?return_to=%2Fadambard%2Flearnxinyminutes-docs"
        class="btn btn-sm btn-with-count tooltipped tooltipped-n"
        aria-label="You must be signed in to fork a repository" rel="nofollow">
        <svg aria-hidden="true" class="octicon octicon-repo-forked" height="16" version="1.1" viewBox="0 0 10 16" width="10"><path fill-rule="evenodd" d="M8 1a1.993 1.993 0 0 0-1 3.72V6L5 8 3 6V4.72A1.993 1.993 0 0 0 2 1a1.993 1.993 0 0 0-1 3.72V6.5l3 3v1.78A1.993 1.993 0 0 0 5 15a1.993 1.993 0 0 0 1-3.72V9.5l3-3V4.72A1.993 1.993 0 0 0 8 1zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3 10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3-10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
        Fork
      </a>

    <a href="/adambard/learnxinyminutes-docs/network" class="social-count"
       aria-label="1609 users forked this repository">
      1,609
    </a>
  </li>
</ul>

    <h1 class="public ">
  <svg aria-hidden="true" class="octicon octicon-repo" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
  <span class="author" itemprop="author"><a href="/adambard" class="url fn" rel="author">adambard</a></span><!--
--><span class="path-divider">/</span><!--
--><strong itemprop="name"><a href="/adambard/learnxinyminutes-docs" data-pjax="#js-repo-pjax-container">learnxinyminutes-docs</a></strong>

</h1>

  </div>
  <div class="container">
    
<nav class="reponav js-repo-nav js-sidenav-container-pjax"
     itemscope
     itemtype="http://schema.org/BreadcrumbList"
     role="navigation"
     data-pjax="#js-repo-pjax-container">

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a href="/adambard/learnxinyminutes-docs" class="js-selected-navigation-item selected reponav-item" data-hotkey="g c" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches /adambard/learnxinyminutes-docs" itemprop="url">
      <svg aria-hidden="true" class="octicon octicon-code" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M9.5 3L8 4.5 11.5 8 8 11.5 9.5 13 14 8 9.5 3zm-5 0L0 8l4.5 5L6 11.5 2.5 8 6 4.5 4.5 3z"/></svg>
      <span itemprop="name">Code</span>
      <meta itemprop="position" content="1">
</a>  </span>

    <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
      <a href="/adambard/learnxinyminutes-docs/issues" class="js-selected-navigation-item reponav-item" data-hotkey="g i" data-selected-links="repo_issues repo_labels repo_milestones /adambard/learnxinyminutes-docs/issues" itemprop="url">
        <svg aria-hidden="true" class="octicon octicon-issue-opened" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"/></svg>
        <span itemprop="name">Issues</span>
        <span class="counter">95</span>
        <meta itemprop="position" content="2">
</a>    </span>

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a href="/adambard/learnxinyminutes-docs/pulls" class="js-selected-navigation-item reponav-item" data-hotkey="g p" data-selected-links="repo_pulls /adambard/learnxinyminutes-docs/pulls" itemprop="url">
      <svg aria-hidden="true" class="octicon octicon-git-pull-request" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
      <span itemprop="name">Pull requests</span>
      <span class="counter">19</span>
      <meta itemprop="position" content="3">
</a>  </span>

  <a href="/adambard/learnxinyminutes-docs/projects" class="js-selected-navigation-item reponav-item" data-selected-links="repo_projects new_repo_project repo_project /adambard/learnxinyminutes-docs/projects">
    <svg aria-hidden="true" class="octicon octicon-project" height="16" version="1.1" viewBox="0 0 15 16" width="15"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1z"/></svg>
    Projects
    <span class="counter">0</span>
</a>


  <a href="/adambard/learnxinyminutes-docs/pulse" class="js-selected-navigation-item reponav-item" data-selected-links="pulse /adambard/learnxinyminutes-docs/pulse">
    <svg aria-hidden="true" class="octicon octicon-pulse" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M11.5 8L8.8 5.4 6.6 8.5 5.5 1.6 2.38 8H0v2h3.6l.9-1.8.9 5.4L9 8.5l1.6 1.5H14V8z"/></svg>
    Pulse
</a>
  <a href="/adambard/learnxinyminutes-docs/graphs" class="js-selected-navigation-item reponav-item" data-selected-links="repo_graphs repo_contributors /adambard/learnxinyminutes-docs/graphs">
    <svg aria-hidden="true" class="octicon octicon-graph" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M16 14v1H0V0h1v14h15zM5 13H3V8h2v5zm4 0H7V3h2v10zm4 0h-2V6h2v7z"/></svg>
    Graphs
</a>

</nav>

  </div>
</div>

<div class="container new-discussion-timeline experiment-repo-nav">
  <div class="repository-content">

    

<a href="/adambard/learnxinyminutes-docs/blob/9e8a3d73b687b3b4ee3558ceef2c1944f7d4051c/CHICKEN.html.markdown" class="d-none js-permalink-shortcut" data-hotkey="y">Permalink</a>

<!-- blob contrib key: blob_contributors:v21:c50b550597e461b1bb168e6edb5a3303 -->

<div class="file-navigation js-zeroclipboard-container">
  
<div class="select-menu branch-select-menu js-menu-container js-select-menu float-left">
  <button class="btn btn-sm select-menu-button js-menu-target css-truncate" data-hotkey="w"
    
    type="button" aria-label="Switch branches or tags" tabindex="0" aria-haspopup="true">
    <i>Branch:</i>
    <span class="js-select-button css-truncate-target">master</span>
  </button>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax aria-hidden="true">

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <svg aria-label="Close" class="octicon octicon-x js-menu-close" height="16" role="img" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
        <span class="select-menu-title">Switch branches/tags</span>
      </div>

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Filter branches/tags" id="context-commitish-filter-field" class="form-control js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" data-filter-placeholder="Filter branches/tags" class="js-select-menu-tab" role="tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" data-filter-placeholder="Find a tag…" class="js-select-menu-tab" role="tab">Tags</a>
            </li>
          </ul>
        </div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches" role="menu">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/adambard/learnxinyminutes-docs/blob/master-cn/CHICKEN.html.markdown"
               data-name="master-cn"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                master-cn
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/adambard/learnxinyminutes-docs/blob/master-es/CHICKEN.html.markdown"
               data-name="master-es"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                master-es
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open selected"
               href="/adambard/learnxinyminutes-docs/blob/master/CHICKEN.html.markdown"
               data-name="master"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                master
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/adambard/learnxinyminutes-docs/blob/new-contributing/CHICKEN.html.markdown"
               data-name="new-contributing"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                new-contributing
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/adambard/learnxinyminutes-docs/blob/p6-array2list/CHICKEN.html.markdown"
               data-name="p6-array2list"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                p6-array2list
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/adambard/learnxinyminutes-docs/blob/revert-1115-master/CHICKEN.html.markdown"
               data-name="revert-1115-master"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                revert-1115-master
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/adambard/learnxinyminutes-docs/blob/revert-1936-master/CHICKEN.html.markdown"
               data-name="revert-1936-master"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                revert-1936-master
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/adambard/learnxinyminutes-docs/blob/upstream/CHICKEN.html.markdown"
               data-name="upstream"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                upstream
              </span>
            </a>
        </div>

          <div class="select-menu-no-results">Nothing to show</div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div>

    </div>
  </div>
</div>

  <div class="BtnGroup float-right">
    <a href="/adambard/learnxinyminutes-docs/find/master"
          class="js-pjax-capture-input btn btn-sm BtnGroup-item"
          data-pjax
          data-hotkey="t">
      Find file
    </a>
    <button aria-label="Copy file path to clipboard" class="js-zeroclipboard btn btn-sm BtnGroup-item tooltipped tooltipped-s" data-copied-hint="Copied!" type="button">Copy path</button>
  </div>
  <div class="breadcrumb js-zeroclipboard-target">
    <span class="repo-root js-repo-root"><span class="js-path-segment"><a href="/adambard/learnxinyminutes-docs"><span>learnxinyminutes-docs</span></a></span></span><span class="separator">/</span><strong class="final-path">CHICKEN.html.markdown</strong>
  </div>
</div>



  <div class="commit-tease">
      <span class="float-right">
        <a class="commit-tease-sha" href="/adambard/learnxinyminutes-docs/commit/28a62c0d3c0d7f31eda2d9baaf7c76d3823c8fd3" data-pjax>
          28a62c0
        </a>
        <relative-time datetime="2016-10-31T02:57:39Z">Oct 31, 2016</relative-time>
      </span>
      <div>
        <img alt="" class="avatar" data-canonical-src="https://0.gravatar.com/avatar/d704142956e00cd793cbe21e3c35301e?d=https%3A%2F%2Fassets-cdn.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png&amp;r=x&amp;s=140" height="20" src="https://camo.githubusercontent.com/0479714f90118260338c62c3ce15e8dcd1478f07/68747470733a2f2f302e67726176617461722e636f6d2f6176617461722f64373034313432393536653030636437393363626532316533633335333031653f643d68747470732533412532462532466173736574732d63646e2e6769746875622e636f6d253246696d6167657325324667726176617461727325324667726176617461722d757365722d3432302e706e6726723d7826733d313430" width="20" />
        <span class="user-mention">Amru Eliwat</span>
          <a href="/adambard/learnxinyminutes-docs/commit/28a62c0d3c0d7f31eda2d9baaf7c76d3823c8fd3" class="message" data-pjax="true" title="Corrected small spelling error">Corrected small spelling error</a>
      </div>

    <div class="commit-tease-contributors">
      <button type="button" class="btn-link muted-link contributors-toggle" data-facebox="#blob_contributors_box">
        <strong>1</strong>
         contributor
      </button>
      
    </div>

    <div id="blob_contributors_box" style="display:none">
      <h2 class="facebox-header" data-facebox-id="facebox-header">Users who have contributed to this file</h2>
      <ul class="facebox-user-list" data-facebox-id="facebox-description">
          <li class="facebox-user-list-item">
            <img alt="@deewakar" height="24" src="https://avatars1.githubusercontent.com/u/2121215?v=3&amp;s=48" width="24" />
            <a href="/deewakar">deewakar</a>
          </li>
      </ul>
    </div>
  </div>

<div class="file">
  <div class="file-header">
  <div class="file-actions">

    <div class="BtnGroup">
      <a href="/adambard/learnxinyminutes-docs/raw/master/CHICKEN.html.markdown" class="btn btn-sm BtnGroup-item" id="raw-url">Raw</a>
        <a href="/adambard/learnxinyminutes-docs/blame/master/CHICKEN.html.markdown" class="btn btn-sm js-update-url-with-hash BtnGroup-item" data-hotkey="b">Blame</a>
      <a href="/adambard/learnxinyminutes-docs/commits/master/CHICKEN.html.markdown" class="btn btn-sm BtnGroup-item" rel="nofollow">History</a>
    </div>


        <button type="button" class="btn-octicon disabled tooltipped tooltipped-nw"
          aria-label="You must be signed in to make or propose changes">
          <svg aria-hidden="true" class="octicon octicon-pencil" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M0 12v3h3l8-8-3-3-8 8zm3 2H1v-2h1v1h1v1zm10.3-9.3L12 6 9 3l1.3-1.3a.996.996 0 0 1 1.41 0l1.59 1.59c.39.39.39 1.02 0 1.41z"/></svg>
        </button>
        <button type="button" class="btn-octicon btn-octicon-danger disabled tooltipped tooltipped-nw"
          aria-label="You must be signed in to make or propose changes">
          <svg aria-hidden="true" class="octicon octicon-trashcan" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M11 2H9c0-.55-.45-1-1-1H5c-.55 0-1 .45-1 1H2c-.55 0-1 .45-1 1v1c0 .55.45 1 1 1v9c0 .55.45 1 1 1h7c.55 0 1-.45 1-1V5c.55 0 1-.45 1-1V3c0-.55-.45-1-1-1zm-1 12H3V5h1v8h1V5h1v8h1V5h1v8h1V5h1v9zm1-10H2V3h9v1z"/></svg>
        </button>
  </div>

  <div class="file-info">
      520 lines (399 sloc)
      <span class="file-info-divider"></span>
    17.3 KB
  </div>
</div>

  
  <div id="readme" class="readme blob instapaper_body">
    <article class="markdown-body entry-content" itemprop="text"><table data-table-type="yaml-metadata">
  <thead>
  <tr>
  <th>language</th>

  <th>filename</th>

  <th>contributors</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><div>CHICKEN</div></td>

  <td><div>CHICKEN.scm</div></td>

  <td><div><table>
  <tbody>
  <tr>
  <td><div><table>
  <tbody>
  <tr>
  <td><div>Diwakar Wagle</div></td>

  <td><div><a href="https://github.com/deewakar">https://github.com/deewakar</a></div></td>
  </tr>
  </tbody>
</table></div></td>
  </tr>
  </tbody>
</table></div></td>
  </tr>
  </tbody>
</table>

<p>CHICKEN is an implementation of Scheme programming language that can
compile Scheme programs to C code as well as interpret them. CHICKEN
supports RSR5 and RSR7 (work in progress) standards and many extensions.</p>
<div class="highlight highlight-source-scheme"><pre><span class="pl-c"><span class="pl-c">;</span>; #!/usr/bin/env csi -s</span>

<span class="pl-c"><span class="pl-c">;</span>; Run the CHICKEN REPL in the commandline as follows :</span>
<span class="pl-c"><span class="pl-c">;</span>; $ csi</span>

<span class="pl-c"><span class="pl-c">;</span>;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;</span>
<span class="pl-c"><span class="pl-c">;</span> 0. Syntax</span>
<span class="pl-c"><span class="pl-c">;</span>;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;</span>

<span class="pl-c"><span class="pl-c">;</span>; Single line comments start with a semicolon</span>

#| Block comments
   can span multiple lines and...
   #| can be nested
   |#
|#

<span class="pl-c"><span class="pl-c">;</span>; S-expression comments are used to comment out expressions</span>
#<span class="pl-c"><span class="pl-c">;</span> (display "nothing")    ; discard this expression </span>

<span class="pl-c"><span class="pl-c">;</span>; CHICKEN has two fundamental pieces of syntax: Atoms and S-expressions</span>
<span class="pl-c"><span class="pl-c">;</span>; an atom is something that evaluates to itself</span>
<span class="pl-c"><span class="pl-c">;</span>; all builtin data types viz. numbers, chars, booleans, strings etc. are atoms</span>
<span class="pl-c"><span class="pl-c">;</span>; Furthermore an atom can be a symbol, an identifier, a keyword, a procedure</span>
<span class="pl-c"><span class="pl-c">;</span>; or the empty list (also called null)</span>
<span class="pl-c1">'athing</span>              <span class="pl-c"><span class="pl-c">;</span>; =&gt; athing </span>
<span class="pl-s">'+</span>                   <span class="pl-c"><span class="pl-c">;</span>; =&gt; + </span>
+                    <span class="pl-c"><span class="pl-c">;</span>; =&gt; &lt;procedure C_plus&gt;</span>

<span class="pl-c"><span class="pl-c">;</span>; S-expressions (short for symbolic expressions) consists of one or more atoms</span>
(<span class="pl-k">quote</span> <span class="pl-s">+</span>)            <span class="pl-c"><span class="pl-c">;</span>; =&gt; + ; another way of writing '+</span>
(<span class="pl-k">+</span> <span class="pl-c1">1</span> <span class="pl-c1">2</span> <span class="pl-c1">3</span>)            <span class="pl-c"><span class="pl-c">;</span>; =&gt; 6 ; this S-expression evaluates to a function call</span>
<span class="pl-s">'</span>(<span class="pl-k">+</span> <span class="pl-c1">1</span> <span class="pl-c1">2</span> <span class="pl-c1">3</span>)           <span class="pl-c"><span class="pl-c">;</span>; =&gt; (+ 1 2 3) ; evaluates to a list </span>


<span class="pl-c"><span class="pl-c">;</span>;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;</span>
<span class="pl-c"><span class="pl-c">;</span> 1. Primitive Datatypes and Operators </span>
<span class="pl-c"><span class="pl-c">;</span>;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;</span>

<span class="pl-c"><span class="pl-c">;</span>; Numbers</span>
99999999999999999999 <span class="pl-c"><span class="pl-c">;</span>; integers</span>
#b1010               <span class="pl-c"><span class="pl-c">;</span>; binary ; =&gt; 10</span>
#o10                 <span class="pl-c"><span class="pl-c">;</span>; octal  ; =&gt; 8</span>
#x8ded               <span class="pl-c"><span class="pl-c">;</span>; hexadecimal ; =&gt; 36333</span>
3.14                 <span class="pl-c"><span class="pl-c">;</span>; real</span>
6.02e+23
3/4                  <span class="pl-c"><span class="pl-c">;</span>; rational</span>

<span class="pl-c"><span class="pl-c">;</span>;Characters and Strings</span>
#\A                  <span class="pl-c"><span class="pl-c">;</span>; A char</span>
<span class="pl-s"><span class="pl-pds">"</span>Hello, World!<span class="pl-pds">"</span></span>      <span class="pl-c"><span class="pl-c">;</span>; strings are fixed-length arrays of characters</span>

<span class="pl-c"><span class="pl-c">;</span>; Booleans</span>
#t                  <span class="pl-c"><span class="pl-c">;</span>; true</span>
#f                  <span class="pl-c"><span class="pl-c">;</span>; false</span>

<span class="pl-c"><span class="pl-c">;</span>; Function call is written as (f x y z ...)</span>
<span class="pl-c"><span class="pl-c">;</span>; where f is a function and x,y,z, ... are arguments</span>
(print <span class="pl-s"><span class="pl-pds">"</span>Hello, World!<span class="pl-pds">"</span></span>)    <span class="pl-c"><span class="pl-c">;</span>; =&gt; Hello, World!</span>
<span class="pl-c"><span class="pl-c">;</span>; formatted output</span>
(printf <span class="pl-s"><span class="pl-pds">"</span>Hello, ~a.<span class="pl-cce">\n</span><span class="pl-pds">"</span></span> <span class="pl-s"><span class="pl-pds">"</span>World<span class="pl-pds">"</span></span>)  <span class="pl-c"><span class="pl-c">;</span>; =&gt; Hello, World.</span>

<span class="pl-c"><span class="pl-c">;</span>; print commandline arguments</span>
(<span class="pl-c1">map</span> print (command-line-arguments)) 

(<span class="pl-c1">list</span> <span class="pl-c1">'foo</span> <span class="pl-c1">'bar</span> <span class="pl-c1">'baz</span>)          <span class="pl-c"><span class="pl-c">;</span>; =&gt; (foo bar baz)</span>
(string-append <span class="pl-s"><span class="pl-pds">"</span>pine<span class="pl-pds">"</span></span> <span class="pl-s"><span class="pl-pds">"</span>apple<span class="pl-pds">"</span></span>) <span class="pl-c"><span class="pl-c">;</span>; =&gt; "pineapple"</span>
(string-ref <span class="pl-s"><span class="pl-pds">"</span>tapioca<span class="pl-pds">"</span></span> <span class="pl-c1">3</span>)       <span class="pl-c"><span class="pl-c">;</span>; =&gt; #\i;; character 'i' is at index 3</span>
(<span class="pl-c1">string-&gt;list</span> <span class="pl-s"><span class="pl-pds">"</span>CHICKEN<span class="pl-pds">"</span></span>)       <span class="pl-c"><span class="pl-c">;</span>; =&gt; (#\C #\H #\I #\C #\K #\E #\N)</span>
(string-&gt;intersperse <span class="pl-s">'</span>(<span class="pl-s"><span class="pl-pds">"</span>1<span class="pl-pds">"</span></span> <span class="pl-s"><span class="pl-pds">"</span>2<span class="pl-pds">"</span></span>) <span class="pl-s"><span class="pl-pds">"</span>:<span class="pl-pds">"</span></span>) <span class="pl-c"><span class="pl-c">;</span>; =&gt; "1:2"</span>
(string-split <span class="pl-s"><span class="pl-pds">"</span>1:2:3<span class="pl-pds">"</span></span> <span class="pl-s"><span class="pl-pds">"</span>:<span class="pl-pds">"</span></span>)     <span class="pl-c"><span class="pl-c">;</span>; =&gt; ("1" "2" "3")</span>


<span class="pl-c"><span class="pl-c">;</span>; Predicates are special functions that return boolean values</span>
(<span class="pl-c1">atom?</span> <span class="pl-c1">#t</span>)                <span class="pl-c"><span class="pl-c">;</span>; =&gt; #t</span>

(<span class="pl-c1">symbol?</span> <span class="pl-c1">#t</span>)              <span class="pl-c"><span class="pl-c">;</span>; =&gt; #f</span>

(<span class="pl-c1">symbol?</span> <span class="pl-s">'+</span>)              <span class="pl-c"><span class="pl-c">;</span>; =&gt; #t</span>

(<span class="pl-c1">procedure?</span> +)            <span class="pl-c"><span class="pl-c">;</span>; =&gt; #t</span>

(<span class="pl-c1">pair?</span> <span class="pl-s">'</span>(<span class="pl-c1">1</span> <span class="pl-c1">2</span>))            <span class="pl-c"><span class="pl-c">;</span>; =&gt; #t</span>

(<span class="pl-c1">pair?</span> <span class="pl-s">'</span>(<span class="pl-c1">1</span> <span class="pl-c1">2</span> . <span class="pl-c1">3</span>))        <span class="pl-c"><span class="pl-c">;</span>; =&gt; #t</span>

(<span class="pl-c1">pair?</span> <span class="pl-c1">'()</span>)               <span class="pl-c"><span class="pl-c">;</span>; =&gt; #f</span>

(<span class="pl-c1">list?</span> <span class="pl-c1">'()</span>)               <span class="pl-c"><span class="pl-c">;</span>; =&gt; #t</span>


<span class="pl-c"><span class="pl-c">;</span>; Some arithmetic operations</span>

(<span class="pl-k">+</span> <span class="pl-c1">1</span> <span class="pl-c1">1</span>)                   <span class="pl-c"><span class="pl-c">;</span>; =&gt; 2</span>
(<span class="pl-k">-</span> <span class="pl-c1">8</span> <span class="pl-c1">1</span>)                   <span class="pl-c"><span class="pl-c">;</span>; =&gt; 7</span>
(<span class="pl-k">*</span> <span class="pl-c1">10</span> <span class="pl-c1">2</span>)                  <span class="pl-c"><span class="pl-c">;</span>; =&gt; 20</span>
(<span class="pl-c1">expt</span> <span class="pl-c1">2</span> <span class="pl-c1">3</span>)                <span class="pl-c"><span class="pl-c">;</span>; =&gt; 8</span>
(<span class="pl-c1">remainder</span> <span class="pl-c1">5</span> <span class="pl-c1">2</span>)           <span class="pl-c"><span class="pl-c">;</span>; =&gt; 1</span>
(<span class="pl-k">/</span> <span class="pl-c1">35</span> <span class="pl-c1">5</span>)                  <span class="pl-c"><span class="pl-c">;</span>; =&gt; 7</span>
(<span class="pl-k">/</span> <span class="pl-c1">1</span> <span class="pl-c1">3</span>)                   <span class="pl-c"><span class="pl-c">;</span>; =&gt; 0.333333333333333</span>

<span class="pl-c"><span class="pl-c">;</span>;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;</span>
<span class="pl-c"><span class="pl-c">;</span> 2. Variables</span>
<span class="pl-c"><span class="pl-c">;</span>;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;</span>

<span class="pl-c"><span class="pl-c">;</span>; You can create variables with define</span>
<span class="pl-c"><span class="pl-c">;</span>; A variable name can use any character except: ()[]{}",'`;#\</span>
(<span class="pl-k">define</span> <span class="pl-smi">myvar</span> 5)
myvar        <span class="pl-c"><span class="pl-c">;</span>; =&gt; 5</span>

<span class="pl-c"><span class="pl-c">;</span>; Alias to a procedure</span>
(<span class="pl-k">define</span> ** expt)
(** <span class="pl-c1">2</span> <span class="pl-c1">3</span>)     <span class="pl-c"><span class="pl-c">;</span>; =&gt; 8</span>

<span class="pl-c"><span class="pl-c">;</span>; Accessing an undefined variable raises an exception</span>
s            <span class="pl-c"><span class="pl-c">;</span>; =&gt; Error: unbound variable: s</span>

<span class="pl-c"><span class="pl-c">;</span>; Local binding</span>
(<span class="pl-k">let</span> ((me <span class="pl-s"><span class="pl-pds">"</span>Bob<span class="pl-pds">"</span></span>))
  (print me))     <span class="pl-c"><span class="pl-c">;</span>; =&gt; Bob</span>

(print me)        <span class="pl-c"><span class="pl-c">;</span>; =&gt; Error: unbound variable: me</span>

<span class="pl-c"><span class="pl-c">;</span>; Assign a new value to previously defined variable</span>
(<span class="pl-k">set!</span> myvar <span class="pl-c1">10</span>) 
myvar             <span class="pl-c"><span class="pl-c">;</span>; =&gt; 10</span>


<span class="pl-c"><span class="pl-c">;</span>;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;</span>
<span class="pl-c"><span class="pl-c">;</span> 3. Collections</span>
<span class="pl-c"><span class="pl-c">;</span>;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;</span>

<span class="pl-c"><span class="pl-c">;</span>; Pairs</span>
<span class="pl-c"><span class="pl-c">;</span>; 'cons' constructs pairs, </span>
<span class="pl-c"><span class="pl-c">;</span>; 'car' extracts the first element, 'cdr' extracts the rest of the elements</span>
(<span class="pl-c1">cons</span> <span class="pl-c1">'subject</span> <span class="pl-c1">'verb</span>)       <span class="pl-c"><span class="pl-c">;</span>; =&gt; '(subject . verb)</span>
(<span class="pl-c1">car</span> (<span class="pl-c1">cons</span> <span class="pl-c1">'subject</span> <span class="pl-c1">'verb</span>)) <span class="pl-c"><span class="pl-c">;</span>; =&gt; subject</span>
(<span class="pl-c1">cdr</span> (<span class="pl-c1">cons</span> <span class="pl-c1">'subject</span> <span class="pl-c1">'verb</span>)) <span class="pl-c"><span class="pl-c">;</span>; =&gt; verb</span>

<span class="pl-c"><span class="pl-c">;</span>; Lists</span>
<span class="pl-c"><span class="pl-c">;</span>; cons creates a new list if the second item is a list</span>
(<span class="pl-c1">cons</span> <span class="pl-c1">0</span> <span class="pl-c1">'()</span>)         <span class="pl-c"><span class="pl-c">;</span>; =&gt; (0)</span>
(<span class="pl-c1">cons</span> <span class="pl-c1">1</span> (<span class="pl-c1">cons</span> <span class="pl-c1">2</span>  (<span class="pl-c1">cons</span> <span class="pl-c1">3</span> <span class="pl-c1">'()</span>)))    <span class="pl-c"><span class="pl-c">;</span>; =&gt; (1 2 3)</span>
<span class="pl-c"><span class="pl-c">;</span>; 'list' is a convenience variadic constructor for lists</span>
(<span class="pl-c1">list</span> <span class="pl-c1">1</span> <span class="pl-c1">2</span> <span class="pl-c1">3</span>)    <span class="pl-c"><span class="pl-c">;</span>; =&gt; (1 2 3)</span>


<span class="pl-c"><span class="pl-c">;</span>; Use 'append' to append lists together</span>
(<span class="pl-c1">append</span> <span class="pl-s">'</span>(<span class="pl-c1">1</span> <span class="pl-c1">2</span>) <span class="pl-s">'</span>(<span class="pl-c1">3</span> <span class="pl-c1">4</span>)) <span class="pl-c"><span class="pl-c">;</span>; =&gt; (1 2 3 4)</span>

<span class="pl-c"><span class="pl-c">;</span>; Some basic operations on lists</span>
(<span class="pl-c1">map</span> add1 <span class="pl-s">'</span>(<span class="pl-c1">1</span> <span class="pl-c1">2</span> <span class="pl-c1">3</span>))    <span class="pl-c"><span class="pl-c">;</span>; =&gt; (2 3 4)</span>
(<span class="pl-c1">reverse</span> <span class="pl-s">'</span>(<span class="pl-c1">1</span> <span class="pl-c1">3</span> <span class="pl-c1">4</span> <span class="pl-c1">7</span>))   <span class="pl-c"><span class="pl-c">;</span>; =&gt; (7 4 3 1)</span>
(sort <span class="pl-s">'</span>(<span class="pl-c1">11</span> <span class="pl-c1">22</span> <span class="pl-c1">33</span> <span class="pl-c1">44</span>) &gt;)   <span class="pl-c"><span class="pl-c">;</span>; =&gt; (44 33 22 11)</span>

(<span class="pl-k">define</span> <span class="pl-smi">days</span> '(SUN MON FRI))
(<span class="pl-c1">list-ref</span> days <span class="pl-c1">1</span>)      <span class="pl-c"><span class="pl-c">;</span>; =&gt; MON</span>
(<span class="pl-k">set!</span> (<span class="pl-c1">list-ref</span> days <span class="pl-c1">1</span>) <span class="pl-c1">'TUE</span>)
days                   <span class="pl-c"><span class="pl-c">;</span>; =&gt; (SUN TUE FRI)</span>

<span class="pl-c"><span class="pl-c">;</span>; Vectors</span>
<span class="pl-c"><span class="pl-c">;</span>; Vectors are heterogeneous structures whose elements are indexed by integers</span>
<span class="pl-c"><span class="pl-c">;</span>; A Vector typically occupies less space than a list of the same length</span>
<span class="pl-c"><span class="pl-c">;</span>; Random access of an element in a vector is faster than in a list</span>
#(<span class="pl-c1">1</span> <span class="pl-c1">2</span> <span class="pl-c1">3</span>)                     <span class="pl-c"><span class="pl-c">;</span>; =&gt; #(1 2 3) ;; literal syntax</span>
(vector <span class="pl-c1">'a</span> <span class="pl-c1">'b</span> <span class="pl-c1">'c</span>)            <span class="pl-c"><span class="pl-c">;</span>; =&gt; #(a b c) </span>
(<span class="pl-c1">vector?</span> #(<span class="pl-c1">1</span> <span class="pl-c1">2</span> <span class="pl-c1">3</span>))           <span class="pl-c"><span class="pl-c">;</span>; =&gt; #t</span>
(<span class="pl-c1">vector-length</span> #(<span class="pl-c1">1</span> (<span class="pl-c1">2</span>) <span class="pl-s"><span class="pl-pds">"</span>a<span class="pl-pds">"</span></span>)) <span class="pl-c"><span class="pl-c">;</span>; =&gt; 3</span>
(<span class="pl-c1">vector-ref</span> #(<span class="pl-c1">1</span> (<span class="pl-c1">2</span>) (<span class="pl-c1">3</span> <span class="pl-c1">3</span>)) <span class="pl-c1">2</span>)<span class="pl-c"><span class="pl-c">;</span>; =&gt; (3 3)</span>

(<span class="pl-k">define</span> <span class="pl-smi">vec</span> #(<span class="pl-c1">1</span> <span class="pl-c1">2</span> <span class="pl-c1">3</span>))
(<span class="pl-c1">vector-set!</span> vec <span class="pl-c1">2</span> <span class="pl-c1">4</span>)
vec                         <span class="pl-c"><span class="pl-c">;</span>; =&gt; #(1 2 4)</span>

<span class="pl-c"><span class="pl-c">;</span>; Vectors can be created from lists and vice-verca</span>
(<span class="pl-c1">vector-&gt;list</span> #(<span class="pl-c1">1</span> <span class="pl-c1">2</span> <span class="pl-c1">4</span>))     <span class="pl-c"><span class="pl-c">;</span>; =&gt; '(1 2 4)</span>
(<span class="pl-c1">list-&gt;vector</span> <span class="pl-s">'</span>(a b c))     <span class="pl-c"><span class="pl-c">;</span>; =&gt; #(a b c)</span>


<span class="pl-c"><span class="pl-c">;</span>;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;</span>
<span class="pl-c"><span class="pl-c">;</span> 4. Functions</span>
<span class="pl-c"><span class="pl-c">;</span>;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;</span>

<span class="pl-c"><span class="pl-c">;</span>; Use 'lambda' to create functions.</span>
<span class="pl-c"><span class="pl-c">;</span>; A function always returns the value of its last expression</span>
(<span class="pl-k">lambda</span> () "Hello World")   <span class="pl-c"><span class="pl-c">;</span>; =&gt; #&lt;procedure (?)&gt; </span>

<span class="pl-c"><span class="pl-c">;</span>; Use extra parens around function definition to execute </span>
((<span class="pl-k">lambda</span> () "Hello World")) <span class="pl-c"><span class="pl-c">;</span>; =&gt; Hello World ;; argument list is empty</span>

<span class="pl-c"><span class="pl-c">;</span>; A function with an argument</span>
((<span class="pl-k">lambda</span> (<span class="pl-v">x</span>) (<span class="pl-k">*</span> x x)) <span class="pl-c1">3</span>)           <span class="pl-c"><span class="pl-c">;</span>; =&gt; 9</span>
<span class="pl-c"><span class="pl-c">;</span>; A function with two arguments</span>
((<span class="pl-k">lambda</span> (<span class="pl-v">x y</span>) (<span class="pl-k">*</span> x y)) <span class="pl-c1">2</span> <span class="pl-c1">3</span>)       <span class="pl-c"><span class="pl-c">;</span>; =&gt; 6</span>

<span class="pl-c"><span class="pl-c">;</span>; assign a function to a variable</span>
(<span class="pl-k">define</span> <span class="pl-smi">sqr</span> (<span class="pl-k">lambda</span> (<span class="pl-v">x</span>) (<span class="pl-k">*</span> x x)))
sqr                        <span class="pl-c"><span class="pl-c">;</span>; =&gt; #&lt;procedure (sqr x)&gt;</span>
(sqr <span class="pl-c1">3</span>)                    <span class="pl-c"><span class="pl-c">;</span>; =&gt; 9</span>

<span class="pl-c"><span class="pl-c">;</span>; We can shorten this using the function definition syntactic sugar</span>
(<span class="pl-k">define</span> (<span class="pl-en">sqr</span><span class="pl-smi"> x</span>) (<span class="pl-k">*</span> x x))
(sqr <span class="pl-c1">3</span>)                    <span class="pl-c"><span class="pl-c">;</span>; =&gt; 9</span>

<span class="pl-c"><span class="pl-c">;</span>; We can redefine existing procedures</span>
(foldl <span class="pl-c1">cons</span> <span class="pl-c1">'()</span> <span class="pl-s">'</span>(<span class="pl-c1">1</span> <span class="pl-c1">2</span> <span class="pl-c1">3</span> <span class="pl-c1">4</span> <span class="pl-c1">5</span>)) <span class="pl-c"><span class="pl-c">;</span>; =&gt; (((((() . 1) . 2) . 3) . 4) . 5)</span>
(<span class="pl-k">define</span> (<span class="pl-en">foldl</span><span class="pl-smi"> func accu alist</span>)
  (<span class="pl-k">if</span> (<span class="pl-c1">null?</span> alist)
    accu
    (foldl func (func (<span class="pl-c1">car</span> alist) accu) (<span class="pl-c1">cdr</span> alist))))

(foldl <span class="pl-c1">cons</span> <span class="pl-c1">'()</span> <span class="pl-s">'</span>(<span class="pl-c1">1</span> <span class="pl-c1">2</span> <span class="pl-c1">3</span> <span class="pl-c1">4</span> <span class="pl-c1">5</span>))   <span class="pl-c"><span class="pl-c">;</span>; =&gt; (5 4 3 2 1)</span>


<span class="pl-c"><span class="pl-c">;</span>;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;</span>
<span class="pl-c"><span class="pl-c">;</span> 5. Equality</span>
<span class="pl-c"><span class="pl-c">;</span>;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;</span>

<span class="pl-c"><span class="pl-c">;</span>; For numbers use '='</span>
(<span class="pl-k">=</span> <span class="pl-c1">3</span> <span class="pl-c1">3.0</span>)                  <span class="pl-c"><span class="pl-c">;</span>; =&gt; #t</span>
(<span class="pl-k">=</span> <span class="pl-c1">2</span> <span class="pl-c1">1</span>)                    <span class="pl-c"><span class="pl-c">;</span>; =&gt; #f</span>

<span class="pl-c"><span class="pl-c">;</span>; 'eq?' returns #t if two arguments refer to the same object in memory</span>
<span class="pl-c"><span class="pl-c">;</span>; In other words, it's a simple pointer comparision.</span>
(<span class="pl-c1">eq?</span> <span class="pl-c1">'()</span> <span class="pl-c1">'()</span>)              <span class="pl-c"><span class="pl-c">;</span>; =&gt; #t ;; there's only one empty list in memory</span>
(<span class="pl-c1">eq?</span> (<span class="pl-c1">list</span> <span class="pl-c1">3</span>) (<span class="pl-c1">list</span> <span class="pl-c1">3</span>))    <span class="pl-c"><span class="pl-c">;</span>; =&gt; #f ;; not the same object</span>
(<span class="pl-c1">eq?</span> <span class="pl-c1">'yes</span> <span class="pl-c1">'yes</span>)            <span class="pl-c"><span class="pl-c">;</span>; =&gt; #t</span>
(<span class="pl-c1">eq?</span> <span class="pl-c1">3</span> <span class="pl-c1">3</span>)                  <span class="pl-c"><span class="pl-c">;</span>; =&gt; #t ;; don't do this even if it works in this case</span>
(<span class="pl-c1">eq?</span> <span class="pl-c1">3</span> <span class="pl-c1">3.0</span>)                <span class="pl-c"><span class="pl-c">;</span>; =&gt; #f ;; it's better to use '=' for number comparisions</span>
(<span class="pl-c1">eq?</span> <span class="pl-s"><span class="pl-pds">"</span>Hello<span class="pl-pds">"</span></span> <span class="pl-s"><span class="pl-pds">"</span>Hello<span class="pl-pds">"</span></span>)      <span class="pl-c"><span class="pl-c">;</span>; =&gt; #f</span>

<span class="pl-c"><span class="pl-c">;</span>; 'eqv?' is same as 'eq?' all datatypes except numbers and characters</span>
(<span class="pl-c1">eqv?</span> <span class="pl-c1">3</span> <span class="pl-c1">3.0</span>)               <span class="pl-c"><span class="pl-c">;</span>; =&gt; #f</span>
(<span class="pl-c1">eqv?</span> (<span class="pl-c1">expt</span> <span class="pl-c1">2</span> <span class="pl-c1">3</span>) (<span class="pl-c1">expt</span> <span class="pl-c1">2</span> <span class="pl-c1">3</span>)) <span class="pl-c"><span class="pl-c">;</span>; =&gt; #t</span>
(<span class="pl-c1">eqv?</span> <span class="pl-c1">'yes</span> <span class="pl-c1">'yes</span>)           <span class="pl-c"><span class="pl-c">;</span>; =&gt; #t</span>

<span class="pl-c"><span class="pl-c">;</span>; 'equal?' recursively compares the contents of pairs, vectors, and strings,</span>
<span class="pl-c"><span class="pl-c">;</span>; applying eqv? on other objects such as numbers and symbols. </span>
<span class="pl-c"><span class="pl-c">;</span>; A rule of thumb is that objects are generally equal? if they print the same.</span>

(<span class="pl-c1">equal?</span> <span class="pl-s">'</span>(<span class="pl-c1">1</span> <span class="pl-c1">2</span> <span class="pl-c1">3</span>) <span class="pl-s">'</span>(<span class="pl-c1">1</span> <span class="pl-c1">2</span> <span class="pl-c1">3</span>)) <span class="pl-c"><span class="pl-c">;</span>; =&gt; #t</span>
(<span class="pl-c1">equal?</span> #(a b c) #(a b c)) <span class="pl-c"><span class="pl-c">;</span>; =&gt; #t</span>
(<span class="pl-c1">equal?</span> <span class="pl-c1">'a</span> <span class="pl-c1">'a</span>)             <span class="pl-c"><span class="pl-c">;</span>; =&gt; #t</span>
(<span class="pl-c1">equal?</span> <span class="pl-s"><span class="pl-pds">"</span>abc<span class="pl-pds">"</span></span> <span class="pl-s"><span class="pl-pds">"</span>abc<span class="pl-pds">"</span></span>)       <span class="pl-c"><span class="pl-c">;</span>; =&gt; #f</span>

<span class="pl-c"><span class="pl-c">;</span>; In Summary:</span>
<span class="pl-c"><span class="pl-c">;</span>; eq? tests if objects are identical</span>
<span class="pl-c"><span class="pl-c">;</span>; eqv? tests if objects are operationally equivalent</span>
<span class="pl-c"><span class="pl-c">;</span>; equal? tests if objects have same structure and contents</span>

<span class="pl-c"><span class="pl-c">;</span>; Comparing strings for equality</span>
(<span class="pl-c1">string=?</span> <span class="pl-s"><span class="pl-pds">"</span>Hello<span class="pl-pds">"</span></span> <span class="pl-s"><span class="pl-pds">"</span>Hello<span class="pl-pds">"</span></span>) <span class="pl-c"><span class="pl-c">;</span>; =&gt; #t</span>


<span class="pl-c"><span class="pl-c">;</span>;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;</span>
<span class="pl-c"><span class="pl-c">;</span> 6. Control Flow</span>
<span class="pl-c"><span class="pl-c">;</span>;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;</span>

<span class="pl-c"><span class="pl-c">;</span>; Conditionals</span>
(<span class="pl-k">if</span> <span class="pl-c1">#t</span>                     <span class="pl-c"><span class="pl-c">;</span>; test expression</span>
  <span class="pl-s"><span class="pl-pds">"</span>True<span class="pl-pds">"</span></span>                   <span class="pl-c"><span class="pl-c">;</span>; then expression</span>
  <span class="pl-s"><span class="pl-pds">"</span>False<span class="pl-pds">"</span></span>)                 <span class="pl-c"><span class="pl-c">;</span>; else expression</span>
                           <span class="pl-c"><span class="pl-c">;</span>; =&gt; "True"</span>

(<span class="pl-k">if</span> (<span class="pl-k">&gt;</span> <span class="pl-c1">3</span> <span class="pl-c1">2</span>)
  <span class="pl-s"><span class="pl-pds">"</span>yes<span class="pl-pds">"</span></span>
  <span class="pl-s"><span class="pl-pds">"</span>no<span class="pl-pds">"</span></span>)                    <span class="pl-c"><span class="pl-c">;</span>; =&gt; "yes"</span>

<span class="pl-c"><span class="pl-c">;</span>; In conditionals, all values that are not '#f' are treated as true.</span>
<span class="pl-c"><span class="pl-c">;</span>; 0, '(), #() "" , are all true values</span>
(<span class="pl-k">if</span> <span class="pl-c1">0</span>
  <span class="pl-s"><span class="pl-pds">"</span>0 is not false<span class="pl-pds">"</span></span>
  <span class="pl-s"><span class="pl-pds">"</span>0 is false<span class="pl-pds">"</span></span>)            <span class="pl-c"><span class="pl-c">;</span>; =&gt; "0 is not false"</span>

<span class="pl-c"><span class="pl-c">;</span>; 'cond' chains a series of tests and returns as soon as it encounters a true condition</span>
<span class="pl-c"><span class="pl-c">;</span>; 'cond' can be used to simulate 'if/elseif/else' statements</span>
(<span class="pl-k">cond</span> ((<span class="pl-k">&gt;</span> <span class="pl-c1">2</span> <span class="pl-c1">2</span>) <span class="pl-s"><span class="pl-pds">"</span>not true so don't return this<span class="pl-pds">"</span></span>)
      ((<span class="pl-k">&lt;</span> <span class="pl-c1">2</span> <span class="pl-c1">5</span>) <span class="pl-s"><span class="pl-pds">"</span>true, so return this<span class="pl-pds">"</span></span>)
      (<span class="pl-k">else</span> <span class="pl-s"><span class="pl-pds">"</span>returning default<span class="pl-pds">"</span></span>))    <span class="pl-c"><span class="pl-c">;</span>; =&gt; "true, so return this"</span>


<span class="pl-c"><span class="pl-c">;</span>; A case expression is evaluated as follows:</span>
<span class="pl-c"><span class="pl-c">;</span>; The key is evaluated and compared with each datum in sense of 'eqv?',</span>
<span class="pl-c"><span class="pl-c">;</span>; The corresponding clause in the matching datum is evaluated and returned as result</span>
(<span class="pl-k">case</span> (<span class="pl-k">*</span> <span class="pl-c1">2</span> <span class="pl-c1">3</span>)              <span class="pl-c"><span class="pl-c">;</span>; the key is 6</span>
  ((<span class="pl-c1">2</span> <span class="pl-c1">3</span> <span class="pl-c1">5</span> <span class="pl-c1">7</span>) <span class="pl-c1">'prime</span>)       <span class="pl-c"><span class="pl-c">;</span>; datum 1</span>
  ((<span class="pl-c1">1</span> <span class="pl-c1">4</span> <span class="pl-c1">6</span> <span class="pl-c1">8</span>) <span class="pl-c1">'composite</span>))  <span class="pl-c"><span class="pl-c">;</span>; datum 2; matched!</span>
                           <span class="pl-c"><span class="pl-c">;</span>; =&gt; composite</span>

<span class="pl-c"><span class="pl-c">;</span>; case with else clause</span>
(<span class="pl-k">case</span> (<span class="pl-c1">car</span> <span class="pl-s">'</span>(c d))
  ((a e i o u) <span class="pl-c1">'vowel</span>)
  ((w y) <span class="pl-c1">'semivowel</span>)
  (<span class="pl-k">else</span> <span class="pl-c1">'consonant</span>))       <span class="pl-c"><span class="pl-c">;</span>; =&gt;  consonant</span>

<span class="pl-c"><span class="pl-c">;</span>; Boolean expressions</span>
<span class="pl-c"><span class="pl-c">;</span>; 'and' returns the first expression that evaluates to #f</span>
<span class="pl-c"><span class="pl-c">;</span>; otherwise, it returns the result of the last expression</span>
(<span class="pl-k">and</span> <span class="pl-c1">#t</span> <span class="pl-c1">#f</span> (<span class="pl-k">=</span> <span class="pl-c1">2</span> <span class="pl-c1">2.0</span>))                <span class="pl-c"><span class="pl-c">;</span>; =&gt; #f</span>
(<span class="pl-k">and</span> (<span class="pl-k">&lt;</span> <span class="pl-c1">2</span> <span class="pl-c1">5</span>) (<span class="pl-k">&gt;</span> <span class="pl-c1">2</span> <span class="pl-c1">0</span>) <span class="pl-s"><span class="pl-pds">"</span>0 &lt; 2 &lt; 5<span class="pl-pds">"</span></span>)    <span class="pl-c"><span class="pl-c">;</span>; =&gt; "0 &lt; 2 &lt; 5"</span>

<span class="pl-c"><span class="pl-c">;</span>; 'or' returns the first expression that evaluates to #t </span>
<span class="pl-c"><span class="pl-c">;</span>; otherwise the result of the last expression is returned</span>
(<span class="pl-k">or</span> <span class="pl-c1">#f</span> <span class="pl-c1">#t</span> <span class="pl-c1">#f</span>)                        <span class="pl-c"><span class="pl-c">;</span>; =&gt; #t</span>
(<span class="pl-k">or</span> <span class="pl-c1">#f</span> <span class="pl-c1">#f</span> <span class="pl-c1">#f</span>)                        <span class="pl-c"><span class="pl-c">;</span>; =&gt; #f</span>

<span class="pl-c"><span class="pl-c">;</span>; 'when' is like 'if' without the else expression</span>
(when (<span class="pl-c1">positive?</span> <span class="pl-c1">5</span>) <span class="pl-s"><span class="pl-pds">"</span>I'm positive<span class="pl-pds">"</span></span>)  <span class="pl-c"><span class="pl-c">;</span>; =&gt; "I'm positive"</span>

<span class="pl-c"><span class="pl-c">;</span>; 'unless' is equivalent to (when (not &lt;test&gt;) &lt;expr&gt;)</span>
(unless (<span class="pl-c1">null?</span> <span class="pl-s">'</span>(<span class="pl-c1">1</span> <span class="pl-c1">2</span> <span class="pl-c1">3</span>)) <span class="pl-s"><span class="pl-pds">"</span>not null<span class="pl-pds">"</span></span>) <span class="pl-c"><span class="pl-c">;</span>; =&gt; "not null"</span>


<span class="pl-c"><span class="pl-c">;</span>; Loops</span>
<span class="pl-c"><span class="pl-c">;</span>; loops can be created with the help of tail-recursions</span>
(<span class="pl-k">define</span> (<span class="pl-en">loop</span><span class="pl-smi"> count</span>)
  (unless (<span class="pl-k">=</span> count <span class="pl-c1">0</span>)
    (print <span class="pl-s"><span class="pl-pds">"</span>hello<span class="pl-pds">"</span></span>) 
    (loop (sub1 count))))
(loop <span class="pl-c1">4</span>)                             <span class="pl-c"><span class="pl-c">;</span>; =&gt; hello, hello ...</span>

<span class="pl-c"><span class="pl-c">;</span>; Or with a named let</span>
(<span class="pl-k">let</span> loop ((i <span class="pl-c1">0</span>) (limit <span class="pl-c1">5</span>))
  (when (<span class="pl-k">&lt;</span> i limit)
    (printf <span class="pl-s"><span class="pl-pds">"</span>i = ~a<span class="pl-cce">\n</span><span class="pl-pds">"</span></span> i)
    (loop (add1 i) limit)))          <span class="pl-c"><span class="pl-c">;</span>; =&gt; i = 0, i = 1....</span>

<span class="pl-c"><span class="pl-c">;</span>; 'do' is another iteration construct</span>
<span class="pl-c"><span class="pl-c">;</span>; It initializes a set of variables and updates them in each iteration</span>
<span class="pl-c"><span class="pl-c">;</span>; A final expression is evaluated after the exit condition is met</span>
(<span class="pl-k">do</span> ((x <span class="pl-c1">0</span> (add1 x )))            <span class="pl-c"><span class="pl-c">;</span>; initialize x = 0 and add 1 in each iteration</span>
  ((<span class="pl-k">=</span> x <span class="pl-c1">10</span>) (print <span class="pl-s"><span class="pl-pds">"</span>done<span class="pl-pds">"</span></span>))      <span class="pl-c"><span class="pl-c">;</span>; exit condition and final expression</span>
  (print x))                     <span class="pl-c"><span class="pl-c">;</span>; command to execute in each step</span>
                                 <span class="pl-c"><span class="pl-c">;</span>; =&gt; 0,1,2,3....9,done</span>

<span class="pl-c"><span class="pl-c">;</span>; Iteration over lists </span>
(<span class="pl-c1">for-each</span> (<span class="pl-k">lambda</span> (<span class="pl-v">a</span>) (print (<span class="pl-k">*</span> a a)))
          <span class="pl-s">'</span>(<span class="pl-c1">3</span> <span class="pl-c1">5</span> <span class="pl-c1">7</span>))                  <span class="pl-c"><span class="pl-c">;</span>; =&gt; 9, 25, 49</span>

<span class="pl-c"><span class="pl-c">;</span>; 'map' is like for-each but returns a list</span>
(<span class="pl-c1">map</span> add1 <span class="pl-s">'</span>(<span class="pl-c1">11</span> <span class="pl-c1">22</span> <span class="pl-c1">33</span>))               <span class="pl-c"><span class="pl-c">;</span>; =&gt; (12 23 34)</span>


<span class="pl-c"><span class="pl-c">;</span>;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;</span>
<span class="pl-c"><span class="pl-c">;</span> 7. Extensions</span>
<span class="pl-c"><span class="pl-c">;</span>;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;</span>

<span class="pl-c"><span class="pl-c">;</span>; The CHICKEN core is very minimal, but additional features are provided by library extensions known as Eggs.</span>
<span class="pl-c"><span class="pl-c">;</span>; You can install Eggs with 'chicken-install &lt;eggname&gt;' command.</span>

<span class="pl-c"><span class="pl-c">;</span>; 'numbers' egg provides support for full numeric tower.</span>
(require-extension numbers)
<span class="pl-c"><span class="pl-c">;</span>; complex numbers</span>
3+4i                               <span class="pl-c"><span class="pl-c">;</span>; =&gt; 3+2i</span>
<span class="pl-c"><span class="pl-c">;</span>; Supports fractions without falling back to inexact flonums</span>
1/3                                <span class="pl-c"><span class="pl-c">;</span>; =&gt; 1/3</span>
<span class="pl-c"><span class="pl-c">;</span>; provides support for large integers through bignums</span>
(<span class="pl-c1">expt</span> <span class="pl-c1">9</span> <span class="pl-c1">20</span>)                        <span class="pl-c"><span class="pl-c">;</span>; =&gt; 12157665459056928801 </span>
<span class="pl-c"><span class="pl-c">;</span>; And other 'extended' functions</span>
(<span class="pl-c1">log</span> <span class="pl-c1">10</span> (<span class="pl-c1">exp</span> <span class="pl-c1">1</span>))                   <span class="pl-c"><span class="pl-c">;</span>; =&gt; 2.30258509299405</span>
(<span class="pl-c1">numerator</span> 2/3)                    <span class="pl-c"><span class="pl-c">;</span>; =&gt; 2</span>

<span class="pl-c"><span class="pl-c">;</span>; 'utf8' provides unicode support</span>
(require-extension utf8)
<span class="pl-s"><span class="pl-pds">"</span><span class="pl-cce">\u</span>03BBx:(<span class="pl-cce">\u</span>03BC<span class="pl-cce">\u</span>0251.<span class="pl-cce">\u</span>0251<span class="pl-cce">\u</span>2192<span class="pl-cce">\u</span>0251).xx<span class="pl-pds">"</span></span> <span class="pl-c"><span class="pl-c">;</span>; =&gt; "λx:(μɑ.ɑ→ɑ).xx"</span>

<span class="pl-c"><span class="pl-c">;</span>; 'posix' provides file I/O and lots of other services for unix-like operating systems</span>
<span class="pl-c"><span class="pl-c">;</span>; Some of the functions are not available in Windows system,</span>
<span class="pl-c"><span class="pl-c">;</span>; See http://wiki.call-cc.org/man/4/Unit%20posix for more details</span>

<span class="pl-c"><span class="pl-c">;</span>; Open a file to append, open "write only" and create file if it does not exist</span>
(<span class="pl-k">define</span> <span class="pl-smi">outfn</span> (file-open <span class="pl-s"><span class="pl-pds">"</span>chicken-hen.txt<span class="pl-pds">"</span></span> (<span class="pl-k">+</span> open/append open/wronly open/creat)))
<span class="pl-c"><span class="pl-c">;</span>; write some text to the file</span>
(file-write outfn <span class="pl-s"><span class="pl-pds">"</span>Did chicken came before hen?<span class="pl-pds">"</span></span>) 
<span class="pl-c"><span class="pl-c">;</span>; close the file</span>
(file-close outfn)
<span class="pl-c"><span class="pl-c">;</span>; Open the file "read only"</span>
(<span class="pl-k">define</span> <span class="pl-smi">infn</span> (file-open <span class="pl-s"><span class="pl-pds">"</span>chicken-hen.txt<span class="pl-pds">"</span></span> open/rdonly))
<span class="pl-c"><span class="pl-c">;</span>; read some text from the file</span>
(file-read infn <span class="pl-c1">30</span>)         <span class="pl-c"><span class="pl-c">;</span>; =&gt; ("Did chicken came before hen?  ", 28)</span>
(file-close infn)

<span class="pl-c"><span class="pl-c">;</span>; CHICKEN also supports SRFI (Scheme Requests For Implementation) extensions</span>
<span class="pl-c"><span class="pl-c">;</span>; See 'http://srfi.schemers.org/srfi-implementers.html" to see srfi's supported by CHICKEN</span>
(require-extension srfi-1)         <span class="pl-c"><span class="pl-c">;</span>; list library</span>
(filter <span class="pl-c1">odd?</span> <span class="pl-s">'</span>(<span class="pl-c1">1</span> <span class="pl-c1">2</span> <span class="pl-c1">3</span> <span class="pl-c1">4</span> <span class="pl-c1">5</span> <span class="pl-c1">6</span> <span class="pl-c1">7</span>))     <span class="pl-c"><span class="pl-c">;</span>; =&gt; (1 3 5 7)</span>
(count <span class="pl-c1">even?</span> <span class="pl-s">'</span>(<span class="pl-c1">1</span> <span class="pl-c1">2</span> <span class="pl-c1">3</span> <span class="pl-c1">4</span> <span class="pl-c1">5</span>))         <span class="pl-c"><span class="pl-c">;</span>; =&gt; 2</span>
(take <span class="pl-s">'</span>(<span class="pl-c1">12</span> <span class="pl-c1">24</span> <span class="pl-c1">36</span> <span class="pl-c1">48</span> <span class="pl-c1">60</span>) <span class="pl-c1">3</span>)         <span class="pl-c"><span class="pl-c">;</span>; =&gt; (12 24 36)</span>
(drop <span class="pl-s">'</span>(<span class="pl-c1">12</span> <span class="pl-c1">24</span> <span class="pl-c1">36</span> <span class="pl-c1">48</span> <span class="pl-c1">60</span>) <span class="pl-c1">2</span>)         <span class="pl-c"><span class="pl-c">;</span>; =&gt; (36 48 60)</span>
(circular-list <span class="pl-c1">'z</span> <span class="pl-c1">'q</span>)              <span class="pl-c"><span class="pl-c">;</span>; =&gt; z q z q ...</span>

(require-extension srfi-13)        <span class="pl-c"><span class="pl-c">;</span>; string library</span>
(string-reverse <span class="pl-s"><span class="pl-pds">"</span>pan<span class="pl-pds">"</span></span>)             <span class="pl-c"><span class="pl-c">;</span>; =&gt; "nap"</span>
(string-index <span class="pl-s"><span class="pl-pds">"</span>Turkey<span class="pl-pds">"</span></span> <span class="pl-cce">#\k</span>)        <span class="pl-c"><span class="pl-c">;</span>; =&gt; 3</span>
(string-every <span class="pl-c1">char-upper-case?</span> <span class="pl-s"><span class="pl-pds">"</span>CHICKEN<span class="pl-pds">"</span></span>) <span class="pl-c"><span class="pl-c">;</span>; =&gt; #t</span>
(string-join <span class="pl-s">'</span>(<span class="pl-s"><span class="pl-pds">"</span>foo<span class="pl-pds">"</span></span> <span class="pl-s"><span class="pl-pds">"</span>bar<span class="pl-pds">"</span></span> <span class="pl-s"><span class="pl-pds">"</span>baz<span class="pl-pds">"</span></span>) <span class="pl-s"><span class="pl-pds">"</span>:<span class="pl-pds">"</span></span>)    <span class="pl-c"><span class="pl-c">;</span>; =&gt; "foo:bar:baz"</span>


<span class="pl-c"><span class="pl-c">;</span>;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;</span>
<span class="pl-c"><span class="pl-c">;</span> 8. Macros</span>
<span class="pl-c"><span class="pl-c">;</span>;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;</span>

<span class="pl-c"><span class="pl-c">;</span>; A 'for .. in ..' iteration like python, for lists</span>
(<span class="pl-c1">define-syntax</span> for
  (<span class="pl-c1">syntax-rules</span> (in)
                ((for elem in alist body ...)
                 (<span class="pl-c1">for-each</span> (<span class="pl-k">lambda</span> (<span class="pl-v">elem</span>) body ...) alist))))

(for x in <span class="pl-s">'</span>(<span class="pl-c1">2</span> <span class="pl-c1">4</span> <span class="pl-c1">8</span> <span class="pl-c1">16</span>)
     (print x))          <span class="pl-c"><span class="pl-c">;</span>; =&gt; 2, 4, 8, 16</span>

(for chr in (<span class="pl-c1">string-&gt;list</span> <span class="pl-s"><span class="pl-pds">"</span>PENCHANT<span class="pl-pds">"</span></span>)
     (print chr))        <span class="pl-c"><span class="pl-c">;</span>; =&gt; P, E, N, C, H, A, N, T</span>

<span class="pl-c"><span class="pl-c">;</span>; While loop</span>
(<span class="pl-c1">define-syntax</span> while
  (<span class="pl-c1">syntax-rules</span> ()
                ((while <span class="pl-k">cond</span> body ...)
                 (<span class="pl-k">let</span> loop ()
                   (when <span class="pl-k">cond</span>
                     body ...
                     (loop))))))

(<span class="pl-k">let</span> ((str <span class="pl-s"><span class="pl-pds">"</span>PENCHANT<span class="pl-pds">"</span></span>) (i <span class="pl-c1">0</span>))
  (while (<span class="pl-k">&lt;</span> i (string-length str))     <span class="pl-c"><span class="pl-c">;</span>; while (condition)</span>
         (print (string-ref str i))    <span class="pl-c"><span class="pl-c">;</span>; body </span>
         (<span class="pl-k">set!</span> i (add1 i))))           
                                       <span class="pl-c"><span class="pl-c">;</span>; =&gt; P, E, N, C, H, A, N, T</span>

<span class="pl-c"><span class="pl-c">;</span>; Advanced Syntax-Rules Primer -&gt; http://petrofsky.org/src/primer.txt</span>
<span class="pl-c"><span class="pl-c">;</span>; Macro system in chicken -&gt; http://lists.gnu.org/archive/html/chicken-users/2008-04/msg00013.html</span>

<span class="pl-c"><span class="pl-c">;</span>;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;</span>
<span class="pl-c"><span class="pl-c">;</span> 9. Modules</span>
<span class="pl-c"><span class="pl-c">;</span>;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;</span>

<span class="pl-c"><span class="pl-c">;</span>; Also See http://wiki.call-cc.org/man/4/Modules</span>

<span class="pl-c"><span class="pl-c">;</span>; The 'test' module exports a value named 'hello' and a macro named 'greet'</span>
(module test (hello greet)
  (import scheme)

  (<span class="pl-c1">define-syntax</span> greet
    (<span class="pl-c1">syntax-rules</span> ()
      ((_ whom) 
       (<span class="pl-k">begin</span>
         (<span class="pl-c1">display</span> <span class="pl-s"><span class="pl-pds">"</span>Hello, <span class="pl-pds">"</span></span>)
         (<span class="pl-c1">display</span> whom)
         (<span class="pl-c1">display</span> <span class="pl-s"><span class="pl-pds">"</span> !<span class="pl-cce">\n</span><span class="pl-pds">"</span></span>) ) ) ) )

  (<span class="pl-k">define</span> (<span class="pl-en">hello</span>)
    (greet <span class="pl-s"><span class="pl-pds">"</span>world<span class="pl-pds">"</span></span>) )  )

<span class="pl-c"><span class="pl-c">;</span>; we can define our modules in a separate file (say test.scm) and load them to the interpreter with</span>
<span class="pl-c"><span class="pl-c">;</span>;         (load "test.scm")</span>

<span class="pl-c"><span class="pl-c">;</span>; import the module</span>
(import test)
(hello)                <span class="pl-c"><span class="pl-c">;</span>; =&gt; Hello, world !</span>
(greet <span class="pl-s"><span class="pl-pds">"</span>schemers<span class="pl-pds">"</span></span>)     <span class="pl-c"><span class="pl-c">;</span>; =&gt; Hello, schemers !</span>

<span class="pl-c"><span class="pl-c">;</span>; We can compile the module files in to shared libraries by using following command,</span>
<span class="pl-c"><span class="pl-c">;</span>;         csc -s test.scm</span>
<span class="pl-c"><span class="pl-c">;</span>;         (load "test.so")</span>

<span class="pl-c"><span class="pl-c">;</span>; Functors</span>
<span class="pl-c"><span class="pl-c">;</span>; Functors are high level modules that can be parameterized by other modules</span>
<span class="pl-c"><span class="pl-c">;</span>; Following functor requires another module named 'M' that provides a function called 'multiply'</span>
<span class="pl-c"><span class="pl-c">;</span>; The functor itself exports a generic function 'square'</span>
(functor (squaring-functor (M (multiply))) (square)
         (import scheme M) 
         (<span class="pl-k">define</span> (<span class="pl-en">square</span><span class="pl-smi"> x</span>) (multiply x x)))

<span class="pl-c"><span class="pl-c">;</span>; Module 'nums' can be passed as a parameter to 'squaring-functor'</span>
(module nums (multiply) 
        (import scheme)     <span class="pl-c"><span class="pl-c">;</span>; predefined modules</span>
        (<span class="pl-k">define</span> (<span class="pl-en">multiply</span><span class="pl-smi"> x y</span>) (<span class="pl-k">*</span> x y))) 
<span class="pl-c"><span class="pl-c">;</span>; the final module can be imported and used in our program</span>
(module number-squarer <span class="pl-k">=</span> (squaring-functor nums)) 

(import number-squarer)
(square <span class="pl-c1">3</span>)              <span class="pl-c"><span class="pl-c">;</span>; =&gt; 9</span>

<span class="pl-c"><span class="pl-c">;</span>; We can instantiate the functor for other inputs</span>
<span class="pl-c"><span class="pl-c">;</span>; Here's another example module that can be passed to squaring-functor</span>
(module stars (multiply)
        (import chicken scheme)  <span class="pl-c"><span class="pl-c">;</span>; chicken module for the 'use' keyword</span>
        (use srfi-1)             <span class="pl-c"><span class="pl-c">;</span>; we can use external libraries in our module</span>
        (<span class="pl-k">define</span> (<span class="pl-en">multiply</span><span class="pl-smi"> x y</span>)
          (list-tabulate x (lambda _ (list-tabulate y (lambda _ <span class="pl-s">'*</span>))))))
(module star-squarer <span class="pl-k">=</span> (squaring-functor stars))

(import star-squarer)
(square <span class="pl-c1">3</span>)              <span class="pl-c"><span class="pl-c">;</span>; =&gt; ((* * *)(* * *)(* * *))</span>
</pre></div>
<h2><a id="user-content-further-reading" class="anchor" href="#further-reading" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Further Reading</h2>
<ul>
<li><a href="http://wiki.call-cc.org/man/4/The%20User%27s%20Manual">CHICKEN User's Manual</a>.</li>
<li><a href="http://www.schemers.org/Documents/Standards/R5RS">RSR5 standards</a></li>
</ul>
<h2><a id="user-content-extra-info" class="anchor" href="#extra-info" aria-hidden="true"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Extra Info</h2>
<ul>
<li><a href="http://wiki.call-cc.org/chicken-for-programmers-of-other-languages">For programmers of other languages</a></li>
<li><a href="http://plr.sourceforge.net/cgi-bin/plr/launch.py">Compare CHICKEN syntax with other languages</a></li>
</ul>
</article>
  </div>

</div>

<button type="button" data-facebox="#jump-to-line" data-facebox-class="linejump" data-hotkey="l" class="d-none">Jump to Line</button>
<div id="jump-to-line" style="display:none">
  <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="" class="js-jump-to-line-form" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
    <input class="form-control linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" aria-label="Jump to line" autofocus>
    <button type="submit" class="btn">Go</button>
</form></div>

  </div>
  <div class="modal-backdrop js-touch-events"></div>
</div>




    </div>
  </div>

  </div>

      <div class="container site-footer-container">
  <div class="site-footer" role="contentinfo">
    <ul class="site-footer-links float-right">
        <li><a href="https://github.com/contact" data-ga-click="Footer, go to contact, text:contact">Contact GitHub</a></li>
      <li><a href="https://developer.github.com" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li><a href="https://training.github.com" data-ga-click="Footer, go to training, text:training">Training</a></li>
      <li><a href="https://shop.github.com" data-ga-click="Footer, go to shop, text:shop">Shop</a></li>
        <li><a href="https://github.com/blog" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
        <li><a href="https://github.com/about" data-ga-click="Footer, go to about, text:about">About</a></li>

    </ul>

    <a href="https://github.com" aria-label="Homepage" class="site-footer-mark" title="GitHub">
      <svg aria-hidden="true" class="octicon octicon-mark-github" height="24" version="1.1" viewBox="0 0 16 16" width="24"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
</a>
    <ul class="site-footer-links">
      <li>&copy; 2017 <span title="0.05136s from github-fe161-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
        <li><a href="https://github.com/site/terms" data-ga-click="Footer, go to terms, text:terms">Terms</a></li>
        <li><a href="https://github.com/site/privacy" data-ga-click="Footer, go to privacy, text:privacy">Privacy</a></li>
        <li><a href="https://github.com/security" data-ga-click="Footer, go to security, text:security">Security</a></li>
        <li><a href="https://status.github.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
        <li><a href="https://help.github.com" data-ga-click="Footer, go to help, text:help">Help</a></li>
    </ul>
  </div>
</div>



  

  <div id="ajax-error-message" class="ajax-error-message flash flash-error">
    <svg aria-hidden="true" class="octicon octicon-alert" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8.865 1.52c-.18-.31-.51-.5-.87-.5s-.69.19-.87.5L.275 13.5c-.18.31-.18.69 0 1 .19.31.52.5.87.5h13.7c.36 0 .69-.19.86-.5.17-.31.18-.69.01-1L8.865 1.52zM8.995 13h-2v-2h2v2zm0-3h-2V6h2v4z"/></svg>
    <button type="button" class="flash-close js-flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg aria-hidden="true" class="octicon octicon-x" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
    </button>
    You can't perform that action at this time.
  </div>


    <script crossorigin="anonymous" src="https://assets-cdn.github.com/assets/compat-8e19569aacd39e737a14c8515582825f3c90d1794c0e5539f9b525b8eb8b5a8e.js"></script>
    <script crossorigin="anonymous" src="https://assets-cdn.github.com/assets/frameworks-bfb72df02752a3a211da0068c66fda27578fe5420e855a691c73c3910742b831.js"></script>
    <script async="async" crossorigin="anonymous" src="https://assets-cdn.github.com/assets/github-c9964ff202c78067f6df7e4d1bfdc3b4ffa8d7cc6c713e07f2fcf2c16daa694b.js"></script>
    
    
    
    
  <div class="js-stale-session-flash stale-session-flash flash flash-warn flash-banner d-none">
    <svg aria-hidden="true" class="octicon octicon-alert" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8.865 1.52c-.18-.31-.51-.5-.87-.5s-.69.19-.87.5L.275 13.5c-.18.31-.18.69 0 1 .19.31.52.5.87.5h13.7c.36 0 .69-.19.86-.5.17-.31.18-.69.01-1L8.865 1.52zM8.995 13h-2v-2h2v2zm0-3h-2V6h2v4z"/></svg>
    <span class="signed-in-tab-flash">You signed in with another tab or window. <a href="">Reload</a> to refresh your session.</span>
    <span class="signed-out-tab-flash">You signed out in another tab or window. <a href="">Reload</a> to refresh your session.</span>
  </div>
  <div class="facebox" id="facebox" style="display:none;">
  <div class="facebox-popup">
    <div class="facebox-content" role="dialog" aria-labelledby="facebox-header" aria-describedby="facebox-description">
    </div>
    <button type="button" class="facebox-close js-facebox-close" aria-label="Close modal">
      <svg aria-hidden="true" class="octicon octicon-x" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
    </button>
  </div>
</div>


  </body>
</html>

