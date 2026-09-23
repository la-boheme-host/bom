---
title: "[아이유] 이별로부터 내 영혼의 단짝까지"
layout: splash
author_profile: false

---

<!-- 1. 지킬(Liquid) 변수 선언 -->
{% assign latest_post = site.posts.first %}
{% assign latest_img = latest_post.header.overlay_image | default: latest_post.teaser | default: '/assets/images/default-hero.jpg' %}

<!-- CSS 스타일 정의 -->
<style>
  .custom-hero-wrapper {
    width: 100vw;
    position: relative;
    left: 50%;
    right: 50%;
    margin-left: -50vw;
    margin-right: -50vw;
    margin-bottom: 2rem;
    background-color: #000000; /* 투명도 100%일 때 배경 틈새가 뜰 경우를 대비한 어두운 베이스 */
    padding: 5rem 0; 
    overflow: hidden;
  }
  
  /* 배경 이미지용 가상 레이어 */
  .custom-hero-wrapper::before {
    content: "";
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background-image: url('{{ latest_img | relative_url }}');
    background-size: cover;
    background-position: center;
    
    /* [수정 2] 투명도를 1(100%)로 설정하여 배경 색감을 완전히 살림 */
    opacity: 1;
    filter: blur(20px);
    transform: scale(1.15);
    z-index: 1;
  }
  
  .custom-hero-inner {
    position: relative;
    z-index: 2;
    max-width: 1280px;
    margin: 0 auto;
    padding: 0 1em;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 8%; 
  }
  
  /* 왼쪽 텍스트 영역 */
  .custom-hero-text {
    flex: 1.3; 
    text-align: left;
  }
  
  .custom-hero-text h1 {
    font-size: 2.1rem;
    margin-bottom: 1rem;
    color: #ffffff; 
    line-height: 1.3;
    font-weight: 800;
    letter-spacing: -0.5px;
    text-shadow: 0px 2px 10px rgba(0, 0, 0, 0.9); /* 배경이 진해졌으므로 텍스트 그림자를 약간 더 강하게 유지 */
  }
  
  .custom-hero-text p {
    font-size: 1.15rem;
    line-height: 1.6;
    margin-bottom: 2rem;
    color: #ffffff; 
    text-shadow: 0px 1px 6px rgba(0, 0, 0, 0.8);
  }
  /* 버튼 스타일 */
  .custom-hero-btn {
    display: inline-block;
    padding: 12px 25px;
    background-color: transparent;
    color: #ffffff !important; /* 테마의 기본 파란색 링크를 무시하고 흰색을 강제 적용 */
    border: 2px solid #ffffff;
    border-radius: 5px;
    text-decoration: none;
    font-weight: bold;
    transition: all 0.3s ease;
    text-shadow: 0px 1px 3px rgba(0,0,0,0.8);
    box-shadow: 0px 2px 5px rgba(0,0,0,0.4);
  }
  
  .custom-hero-btn:hover {
    background-color: #ffffff;
    color: #222222 !important; /* 마우스 오버 시 기존처럼 어두운 색상 유지 */
    text-shadow: none;
  }

  /* 오른쪽 3D CD 케이스 이미지 영역 */
  .custom-hero-visual {
    flex: 0.7; 
    display: flex;
    justify-content: flex-end; 
    align-items: center;
    perspective: 1200px; 
  }

  /* [수정 1] rotateY를 음수로 변경하여 왼쪽이 화면 안쪽으로 물러나게 만듦 */
  @keyframes floatCD {
    0% {
      transform: rotateY(-18deg) rotateX(5deg) scale(1.05) translateY(0px);
    }
    50% {
      transform: rotateY(-22deg) rotateX(1deg) scale(1.05) translateY(-15px);
    }
    100% {
      transform: rotateY(-18deg) rotateX(5deg) scale(1.05) translateY(0px);
    }
  }
  
  .cd-case-img {
    width: 100%;
    max-width: 380px;
    aspect-ratio: 1 / 1;
    object-fit: cover;
    
    /* 아크릴(플라스틱) 느낌을 살린 밝고 투명한 두께 표현 */
    box-shadow: 
      inset 1px 0px 4px rgba(255, 255, 255, 0.6), /* 표면 안쪽의 부드러운 빛 반사 */
      1px 0px 0px rgba(200, 200, 200, 0.9),       /* 플라스틱 모서리의 쨍한 하이라이트 */
      2px 0px 0px rgba(190, 190, 190, 0.8),       /* 맑은 두께감 1 */
      3px 0px 0px rgba(180, 180, 180, 0.7),       /* 맑은 두께감 2 */
      4px 0px 0px rgba(170, 170, 170, 0.5),       /* 맑은 두께감 3 */
      5px 0px 0px rgba(160, 160, 160, 0.3),       /* 굴절되어 살짝 그림자지는 끝부분 */
      25px 35px 50px rgba(0, 0, 0, 0.5);          /* 바닥에 떨어지는 부드러운 진짜 그림자 */
      
    border-radius: 2px 4px 4px 2px;
    
    animation: floatCD 6s ease-in-out infinite;
    transition: box-shadow 0.6s ease;
  }
  
  .cd-case-img:hover {
    animation-play-state: paused;
    transform: rotateY(-8deg) rotateX(2deg) scale(1.1);
    box-shadow: 
      inset 1px 0px 4px rgba(255, 255, 255, 0.8),
      1px 0px 0px rgba(200, 200, 200, 0.9),       /* 플라스틱 모서리의 쨍한 하이라이트 */
      2px 0px 0px rgba(190, 190, 190, 0.8),       /* 맑은 두께감 1 */
      3px 0px 0px rgba(180, 180, 180, 0.7),       /* 맑은 두께감 2 */
      4px 0px 0px rgba(170, 170, 170, 0.5),       /* 맑은 두께감 3 */
      30px 40px 50px rgba(0, 0, 0, 0.4);
  }
  
@media (max-width: 768px) {
    .custom-hero-inner {
      flex-direction: column;
      padding: 0 2em;
    }
    
    /* 1. 텍스트 영역의 순서를 2번째로 미룹니다. */
    .custom-hero-text {
      order: 2; 
    }
    
    /* 2. 시각(이미지) 영역의 순서를 1번째로 끌어올립니다. */
    .custom-hero-visual {
      order: 1; 
      justify-content: center;
      margin-top: 0;       /* 이미지가 위로 올라갔으므로 위쪽 여백을 없앱니다. */
      margin-bottom: 3rem; /* 텍스트와의 사이에 시원한 간격을 줍니다. */
    }
  }
</style>

<!-- 2. 풀와이드 동적 히어로 영역 HTML -->
<div class="custom-hero-wrapper">
  <div class="custom-hero-inner">
    
    <div class="custom-hero-text">
      <h1>{{ latest_post.title }}</h1>
      <p>{{ latest_post.excerpt | strip_html | truncate: 100 }}</p>
      <a href="{{ latest_post.url | relative_url }}" class="custom-hero-btn">Read more</a>
    </div>
    
    <div class="custom-hero-visual">
      <img src="{{ latest_img | relative_url }}" alt="{{ latest_post.title }}" class="cd-case-img">
    </div>
    
  </div>
</div>

<style>
  /* 기본 여백 제거 및 중앙 정렬 컨테이너 */
  .page__inner-wrap {
    max-width: 100% !important;
    padding-left: 0 !important;
    padding-right: 0 !important;
  }
  .content-container {
    max-width: 1280px;
    margin: 0 auto;
    padding: 0 1em;
  }

  /* =========================================
     랜덤 가사 인트로 영역 CSS (여백 50% 축소)
     ========================================= */
  .custom-intro {
    text-align: center;
    padding: 30px 20px 20px; /* 기존 60px 20px 40px 에서 상하 여백 대폭 감소 */
    margin-bottom: 10px;     /* 기존 20px 에서 10px로 감소 */
  }
  .custom-intro .lyric-text {
    font-style: italic; 
    font-size: 1.2rem;
    color: #333;
    margin-bottom: 15px;
  }
  .custom-intro .lyric-artist {
    font-size: 0.95rem;
    color: #666;
  }

  /* =========================================
     피처 로우 영역 CSS (여백 50% 축소)
     ========================================= */
  .feature-row { 
    display: flex; 
    flex-direction: column; 
    align-items: flex-start; 
    gap: 40px; 
    padding: 30px 0; /* 기존 60px 에서 30px로 상하 간격 감소 */
    border-bottom: 1px solid #f2f3f3; 
  }
  .feature-row:last-of-type { border-bottom: none; }
  
  @media (min-width: 768px) {
    .feature-row { flex-direction: row; }
    .feature-row.reverse { flex-direction: row-reverse; } 
    .feature-row.reverse .feature-text { text-align: right; align-items: flex-end; }
  }
  
  .feature-img { flex: 1; width: 100%; }
  .feature-img img { width: 100%; height: auto; border-radius: 4px; display: block; }
  
  .feature-text { 
    flex: 1; 
    display: flex; 
    flex-direction: column; 
    justify-content: flex-start; 
    align-items: flex-start; 
    padding: 0; 
  }
  .feature-text h2 { margin-top: 0; font-size: 1.5rem; font-weight: bold; margin-bottom: 15px; }
  .feature-text p { color: #494e52; line-height: 1.6; margin-bottom: 25px; }
  
  /* =========================================
     CD 커버 갤러리 영역 CSS 
     ========================================= */
  .custom-gallery-grid { display: grid; gap: 24px; margin-top: 2em; grid-template-columns: repeat(1, 1fr); }
  @media (min-width: 768px) { .custom-gallery-grid { grid-template-columns: repeat(2, 1fr); } }
  @media (min-width: 1024px) { .custom-gallery-grid { grid-template-columns: repeat(4, 1fr); } }
  .custom-gallery-item { position: relative; overflow: hidden; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
  .custom-gallery-item img { width: 100%; aspect-ratio: 1 / 1; object-fit: cover; display: block; transition: transform 0.3s ease; }
  .gallery-overlay { position: absolute; bottom: 0; left: 0; right: 0; background: rgba(0, 0, 0, 0.7); color: #ffffff; padding: 15px; text-align: center; font-weight: bold; font-size: 1rem; transform: translateY(100%); transition: transform 0.3s ease; pointer-events: none; }
  .custom-gallery-item:hover img { transform: scale(1.05); }
  .custom-gallery-item:hover .gallery-overlay { transform: translateY(0); }
  .hidden-item { display: none; }
</style>

<div class="content-container">

  <!-- 랜덤 가사 출력 HTML 영역 -->
  <div class="custom-intro">
    <div class="lyric-text" id="random-lyric-text">"..."</div>
    <div class="lyric-artist" id="random-lyric-artist">- -</div>
  </div>
  
  <!-- 구분선 -->
  <hr style="border: 0; border-top: 1px solid #f2f3f3; margin: 0;">

  <!-- 피처 로우 영역 (시작 마진 50% 축소) -->
  <div style="margin-top: 10px;"> <!-- 기존 20px 에서 10px로 감소 -->
    {% for post in site.posts limit:2 offset:1 %}
      <div class="feature-row {% if forloop.index == 2 %}reverse{% endif %}">
        <div class="feature-img">
          <a href="{{ post.url }}">
            <img src="{{ post.teaser }}" alt="{{ post.title }}">
          </a>
        </div>
        <div class="feature-text">
          <h2>{{ post.title }}</h2>
          <p>{{ post.excerpt | strip_html | truncatewords: 30 }}</p>
          <a href="{{ post.url }}" class="btn btn--danger">Read More</a>
        </div>
      </div>
    {% endfor %}
  </div>

  <!-- 무한 스크롤 갤러리 영역 (상단 마진 50% 축소) -->
  <h2 style="text-align: center; margin-top: 40px; margin-bottom: 20px;">More Music Collection</h2> <!-- 기존 80px 에서 40px로 감소 -->
  
  <div class="custom-gallery-grid" id="gallery-grid">
    {% for post in site.posts offset:3 %}
      {% if post.teaser %}
        <div class="custom-gallery-item gallery-item-card">
          <a href="{{ post.url }}">
            <img src="{{ post.teaser }}" alt="{{ post.title }}">
            <div class="gallery-overlay">{{ post.title }}</div>
          </a>
        </div>
      {% endif %}
    {% endfor %}
  </div>

  <div id="scroll-sentinel" style="height: 20px; margin-top: 40px; margin-bottom: 40px;"></div>

</div>

<!-- 자바스크립트 영역 -->
<script>
  document.addEventListener("DOMContentLoaded", function() {
    
    // 랜덤 가사 자바스크립트 로직 (innerHTML 적용 완료)
    const lyricsList = [
      {% for lyric in site.data.lyrics %}
        { text: "{{ lyric.text }}", artist: "{{ lyric.artist }}" }{% unless forloop.last %},{% endunless %}
      {% endfor %}
    ];

    if (lyricsList.length > 0) {
      const randomIndex = Math.floor(Math.random() * lyricsList.length);
      const selectedLyric = lyricsList[randomIndex];

      document.getElementById('random-lyric-text').innerHTML = '"' + selectedLyric.text + '"';
      document.getElementById('random-lyric-artist').innerHTML = "- " + selectedLyric.artist;
    }

    // 무한 스크롤 자바스크립트 로직
    const items = document.querySelectorAll('.gallery-item-card');
    const sentinel = document.getElementById('scroll-sentinel');
    let currentVisible = 16;
    const loadStep = 16;

    for (let i = 0; i < items.length; i++) {
      if (i >= currentVisible) {
        items[i].classList.add('hidden-item');
      }
    }

    if (items.length <= currentVisible && sentinel) {
      sentinel.style.display = 'none';
    } else if (sentinel) {
      const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            let shown = 0;
            for (let i = 0; i < items.length; i++) {
              if (items[i].classList.contains('hidden-item') && shown < loadStep) { 
                items[i].classList.remove('hidden-item');
                shown++;
                currentVisible++;
              }
            }
            if (currentVisible >= items.length) {
              observer.unobserve(sentinel);
              sentinel.style.display = 'none';
            }
          }
        });
      }, {
        rootMargin: "0px 0px 300px 0px" 
      });
      observer.observe(sentinel);
    }
  });
</script>