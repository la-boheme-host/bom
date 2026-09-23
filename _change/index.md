---
title: "[노리플라이] 그대 걷던길"
layout: splash
author_profile: false
header:
  overlay_image: /assets/images/244/img.jpg
  actions:
    - label: "Read more"
      url: "/244"
# excerpt: "한국 인디 음악의 황금기를 상징하는 팀이자, **완벽한 서정성**을 가진 밴드 노리플라이(no reply)의 2009년 데뷔 정규 1집 [Road]의 타이틀곡, **그대 걷던 길**은 인디록과 포크의 결을 섬세하게 섞어 **노리플라이**를 ‘감성 밴드’의 대명사로 각인시킨 명곡입니다. "
---

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