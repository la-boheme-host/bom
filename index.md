---
masthead_title: "봄 - La bohème by @haanss"
# title: "봄 - La bohème by @haanss"
layout: splash
author_profile: false
---

<!-- 1. 지킬(Liquid) 변수 설정: 3개의 슬라이드 데이터 추출 -->
{% assign post1 = site.posts[0] %}
{% assign img1 = post1.header.overlay_image | default: post1.teaser | default: '/assets/images/default-hero.jpg' %}

{% assign total_posts = site.posts.size %}
{% assign recent_max = total_posts | at_most: 50 %}

<!-- 빌드 시간을 활용한 랜덤 숫자 생성 (최근 50개 중) -->
{% assign rand2 = site.time | date: "%s" | modulo: recent_max %}
{% if rand2 == 0 %}{% assign rand2 = 1 %}{% endif %}
{% assign post2 = site.posts[rand2] | default: site.posts[1] %}
{% assign img2 = post2.header.overlay_image | default: post2.teaser | default: '/assets/images/default-hero.jpg' %}

<!-- 빌드 시간을 활용한 랜덤 숫자 생성 (전체 중) -->
{% assign rand3 = site.time | date: "%N" | modulo: total_posts %}
{% if rand3 == 0 or rand3 == rand2 %}{% assign rand3 = 2 %}{% endif %}
{% assign post3 = site.posts[rand3] | default: site.posts[2] %}
{% assign img3 = post3.header.overlay_image | default: post3.teaser | default: '/assets/images/default-hero.jpg' %}


<!-- 2. CSS 스타일 정의 -->
<style>
  .custom-hero-carousel {
    position: relative;
    width: 100vw;
    left: 50%;
    right: 50%;
    margin-left: -50vw;
    margin-right: -50vw;
    margin-bottom: 2rem;
    background-color: #000000;
    overflow: hidden; 
    /* 🌟 1. 전체 카루셀 영역 높이를 680px로 강제 고정합니다 */
    height: 680px;
  }

  .carousel-track {
    display: flex;
    width: 300%; 
    /* 🌟 2. 부모의 680px 높이를 상속받아 꽉 채웁니다 */
    height: 100%;
    transition: transform 0.6s ease-in-out; 
  }

  .carousel-slide {
    width: 33.3333%;
    position: relative;
    padding: 2.5rem 0;
    display: flex;
    align-items: center; /* 🌟 3. 고정된 680px 높이 내에서 내부 요소를 수직 중앙에 배치합니다 */
    /* padding: 2.5rem 0; 삭제됨 (높이가 고정되었으므로 패딩으로 조절하지 않음) */
  }

  .carousel-slide::before {
    content: "";
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background-image: var(--bg-img);
    background-size: cover;
    background-position: center;
    opacity: 1; 
    filter: blur(40px);
    transform: scale(1.15);
    z-index: 1;
  }

  .custom-hero-inner {
    position: relative;
    z-index: 2;
    width: 100%; /* flex 자식으로서 너비 보장 */
    max-width: 1280px;
    margin: 0 auto;
    padding: 0 1em;
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    gap: 8%;
  }

  /* 🌟 텍스트 상단 여백 설정 🌟 */
  .custom-hero-text { 
    flex: 1.3; 
    text-align: left; 
    align-self: flex-start; /* 텍스트 상자를 위로 끌어올립니다 */
    margin-top: 60px; /* 원하는 상단 여백 수치로 조절하세요 */
  }

  /* 🌟 카테고리 텍스트 디자인 (붉은색) 🌟 */
  .custom-hero-category {
    display: inline-block;
    font-size: 1rem;
    font-weight: 700;
    color: #dd3030; 
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 5px;
    text-shadow: 0px 1px 3px rgba(0, 0, 0, 0.8); 
  }

  .custom-hero-text h1 {
    font-size: 2rem; margin-bottom: 1rem; color: #ffffff;
    line-height: 1.3; font-weight: 800; letter-spacing: -0.5px;
    text-shadow: 0px 2px 10px rgba(0, 0, 0, 0.9);
  }
  .custom-hero-text p {
    font-size: 1.15rem; line-height: 1.6; margin-bottom: 2rem; color: #ffffff;
    text-shadow: 0px 1px 6px rgba(0, 0, 0, 0.8);
  }

  .custom-hero-btn {
    display: inline-block; padding: 12px 25px; background-color: transparent;
    color: #ffffff !important; border: 2px solid #ffffff; border-radius: 5px;
    text-decoration: none; font-weight: bold; transition: all 0.3s ease;
    text-shadow: 0px 1px 3px rgba(0,0,0,0.8); box-shadow: 0px 2px 5px rgba(0,0,0,0.5);
  }
  .custom-hero-btn:hover {
    background-color: #ffffff; color: #222222 !important; text-shadow: none;
  }

  .custom-hero-visual {
    flex: 0.7; display: flex; justify-content: flex-end;
    align-items: flex-start;
    transform: translateX(-30px); 
  }

  .cd-case-img {
    width: 100%; 
    max-width: 380px; 
    aspect-ratio: 7 / 10; 
    object-fit: cover;
    border-radius: 5px; 
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3); 
  }

  .carousel-arrow {
    position: absolute;
    top: 50%;
    transform: translateY(-50%) scaleX(0.5);
    background: transparent;
    color: #ffffff;
    border: none;
    font-size: 5rem;
    font-weight: 300;
    cursor: pointer;
    z-index: 10;
    padding: 1rem;
    opacity: 0.2; 
    transition: opacity 0.3s ease;
  }
  .carousel-arrow:hover { opacity: 1; }

  @media (min-width: 1280px) {
    .carousel-arrow.left { left: calc((100vw - 1280px) / 10); }
    .carousel-arrow.right { right: calc((100vw - 1280px) / 10); }
  }
  @media (max-width: 1279px) {
    .carousel-arrow.left { left: 1vw; }
    .carousel-arrow.right { right: 1vw; }
  }

  .carousel-dots {
    position: absolute; bottom: 1.5rem; left: 50%; transform: translateX(-50%);
    display: flex; gap: 8px; z-index: 10;
  }
  .dot {
    width: 10px; height: 10px; background-color: rgba(255, 255, 255, 0.5);
    border-radius: 50%; cursor: pointer; transition: 0.3s;
  }
  .dot.active { background-color: #ffffff; transform: scale(1.2); }

  @media (max-width: 768px) {
    .custom-hero-inner { 
      flex-direction: column; padding: 0 2em; 
      align-items: center; 
    }
    .custom-hero-text { 
      order: 2; text-align: center; 
      margin-top: 0; /* 🌟 모바일에서는 상단 여백을 초기화하여 디자인 붕괴 방지 */
    }
    .custom-hero-visual { 
      order: 1; justify-content: center; margin-bottom: 3rem; 
      transform: translateX(0);
    }
  }
</style>


<!-- 3. HTML 카루셀 구조 🌟(카테고리 2단 출력 로직 적용)🌟 -->
<div class="custom-hero-carousel">
  <div class="carousel-track" id="track">
    
    <!-- 슬라이드 1 -->
    <div class="carousel-slide" style="--bg-img: url('{{ img1 | relative_url }}')">
      <div class="custom-hero-inner">
        <div class="custom-hero-text">
          <!-- 🌟 카테고리가 2개 이상일 경우 [0]/[1] 형태로 출력 -->
          {% if post1.categories.size > 1 %}
            <span class="custom-hero-category">{{ post1.categories[0] }}/{{ post1.categories[1] }}</span>
          {% elsif post1.categories.size > 0 %}
            <span class="custom-hero-category">{{ post1.categories[0] }}</span>
          {% endif %}
          
          <h1>{{ post1.title }}</h1>
          <p>{{ post1.excerpt | strip_html | truncate: 100 }}</p>
          <a href="{{ post1.url | relative_url }}" class="custom-hero-btn">Read more</a>
        </div>
        <div class="custom-hero-visual">
          <img src="{{ img1 | relative_url }}" alt="{{ post1.title }}" class="cd-case-img">
        </div>
      </div>
    </div>

    <!-- 슬라이드 2 -->
    <div class="carousel-slide" style="--bg-img: url('{{ img2 | relative_url }}')">
      <div class="custom-hero-inner">
        <div class="custom-hero-text">
          {% if post2.categories.size > 1 %}
            <span class="custom-hero-category">{{ post2.categories[0] }}/{{ post2.categories[1] }}</span>
          {% elsif post2.categories.size > 0 %}
            <span class="custom-hero-category">{{ post2.categories[0] }}</span>
          {% endif %}
          
          <h1>{{ post2.title }}</h1>
          <p>{{ post2.excerpt | strip_html | truncate: 100 }}</p>
          <a href="{{ post2.url | relative_url }}" class="custom-hero-btn">Read more</a>
        </div>
        <div class="custom-hero-visual">
          <img src="{{ img2 | relative_url }}" alt="{{ post2.title }}" class="cd-case-img">
        </div>
      </div>
    </div>

    <!-- 슬라이드 3 -->
    <div class="carousel-slide" style="--bg-img: url('{{ img3 | relative_url }}')">
      <div class="custom-hero-inner">
        <div class="custom-hero-text">
          {% if post3.categories.size > 1 %}
            <span class="custom-hero-category">{{ post3.categories[0] }}/{{ post3.categories[1] }}</span>
          {% elsif post3.categories.size > 0 %}
            <span class="custom-hero-category">{{ post3.categories[0] }}</span>
          {% endif %}
          
          <h1>{{ post3.title }}</h1>
          <p>{{ post3.excerpt | strip_html | truncate: 100 }}</p>
          <a href="{{ post3.url | relative_url }}" class="custom-hero-btn">Read more</a>
        </div>
        <div class="custom-hero-visual">
          <img src="{{ img3 | relative_url }}" alt="{{ post3.title }}" class="cd-case-img">
        </div>
      </div>
    </div>

  </div>

  <button class="carousel-arrow left" id="btnPrev">&lt;</button>
  <button class="carousel-arrow right" id="btnNext">&gt;</button>
  
  <div class="carousel-dots">
    <span class="dot active" data-index="0"></span>
    <span class="dot" data-index="1"></span>
    <span class="dot" data-index="2"></span>
  </div>
</div>


<!-- 4. 슬라이드 제어 자바스크립트 -->
<script>
  document.addEventListener('DOMContentLoaded', () => {
    const track = document.getElementById('track');
    const dots = document.querySelectorAll('.dot');
    let currentIndex = 0;
    let timer;

    function goToSlide(index) {
      if (index < 0) index = 2; 
      if (index > 2) index = 0; 
      
      currentIndex = index;
      track.style.transform = `translateX(-${currentIndex * 33.3333}%)`;
      
      dots.forEach(dot => dot.classList.remove('active'));
      dots[currentIndex].classList.add('active');
    }

    document.getElementById('btnNext').addEventListener('click', () => {
      goToSlide(currentIndex + 1);
      resetTimer(); 
    });
    
    document.getElementById('btnPrev').addEventListener('click', () => {
      goToSlide(currentIndex - 1);
      resetTimer();
    });

    dots.forEach((dot, index) => {
      dot.addEventListener('click', () => {
        goToSlide(index);
        resetTimer();
      });
    });

    function startTimer() {
      timer = setInterval(() => goToSlide(currentIndex + 1), 5000);
    }
    
    function resetTimer() {
      clearInterval(timer);
      startTimer();
    }

    startTimer(); 
  });
</script>

<style>
  .page__inner-wrap { max-width: 100% !important; padding-left: 0 !important; padding-right: 0 !important; }
  .content-container { max-width: 1280px; margin: 0 auto; padding: 0 1em; }

  /* 랜덤 가사 영역 CSS */
  .custom-intro { 
    text-align: center; 
    padding: 30px 20px 20px; 
    margin-bottom: 10px; 
  }
  
  .custom-intro .lyric-text { 
    font-style: italic; 
    font-size: 1.2rem; 
    color: #333; 
    margin-bottom: 15px; 
    font-family: 'Noto Serif KR', 'Nanum Myeongjo', 'Batang', '바탕', serif;
  }
  
  .custom-intro .lyric-artist { 
    font-size: 0.95rem; 
    color: #666; 
  }

  /* 피처 로우 영역 CSS */
  .feature-row { display: flex; flex-direction: column; align-items: flex-start; gap: 40px; padding: 30px 0; border-bottom: 1px solid #f2f3f3; }
  .feature-row:last-of-type { border-bottom: none; }
  
  @media (min-width: 768px) {
    .feature-row { flex-direction: row; }
    .feature-row.reverse { flex-direction: row-reverse; } 
    .feature-row.reverse .feature-text { text-align: right; align-items: flex-end; }
  }
  
  .feature-img { flex: 1; width: 100%; }
  .feature-img img { width: 100%; height: auto; border-radius: 4px; display: block; }
  
  .feature-text { flex: 1; display: flex; flex-direction: column; justify-content: flex-start; align-items: flex-start; padding: 0; }
  .feature-text h2 { margin-top: 0; font-size: 1.5rem; font-weight: bold; margin-bottom: 15px; }
  .feature-text p { color: #494e52; line-height: 1.6; margin-bottom: 25px; }
  
  /* 무한 스크롤 갤러리 영역 CSS */
  .custom-gallery-grid { display: grid; gap: 24px; margin-top: 2em; grid-template-columns: repeat(1, 1fr); }
  @media (min-width: 768px) { .custom-gallery-grid { grid-template-columns: repeat(2, 1fr); } }
  @media (min-width: 1024px) { .custom-gallery-grid { grid-template-columns: repeat(4, 1fr); } }
  .custom-gallery-item { position: relative; overflow: hidden; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
  .custom-gallery-item img { width: 100%; aspect-ratio: 7 / 10; object-fit: cover; display: block; transition: transform 0.3s ease; }
  .gallery-overlay { position: absolute; bottom: 0; left: 0; right: 0; background: rgba(0, 0, 0, 0.7); color: #ffffff; padding: 15px; text-align: center; font-weight: bold; font-size: 1rem; transform: translateY(100%); transition: transform 0.3s ease; pointer-events: none; }
  .custom-gallery-item:hover img { transform: scale(1.05); }
  .custom-gallery-item:hover .gallery-overlay { transform: translateY(0); }
  .hidden-item { display: none; }
</style>

<div class="content-container">

  <div class="custom-intro">
    <div class="lyric-text" id="random-lyric-text">"..."</div>
    <div class="lyric-artist" id="random-lyric-artist">- -</div>
  </div>
  
  <hr style="border: 0; border-top: 1px solid #f2f3f3; margin: 0;">

  <div style="margin-top: 10px;"> 
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

  <h2 style="text-align: center; margin-top: 40px; margin-bottom: 20px;">the Poster Collection</h2> 
  
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