
// 1. Hide / Unhide Funksiyasi
function toggleSecret() {
    const secretBox = document.getElementById('secretBox');
    secretBox.classList.toggle('show');
}

// 2. Tilni o'zgartirish va lang atributini boshqarish
function switchLanguage(lang) {
    // HTML tegining lang atributini o'zgartiramiz
    document.documentElement.setAttribute('lang', lang);

    const uzElements = document.querySelectorAll('.lang-uz');
    const enElements = document.querySelectorAll('.lang-en');

    if (lang === 'en') {
        uzElements.forEach(el => el.style.display = 'none');
        enElements.forEach(el => el.style.display = 'inline-block');
    } else {
        enElements.forEach(el => el.style.display = 'none');
        uzElements.forEach(el => el.style.display = 'inline-block');
    }

    // Tanlangan tilni brauzerda kuki sifatida saqlab qolamiz (30 kunga)
    document.cookie = "site_lang=" + lang + "; max-age=" + (60 * 60 * 24 * 30) + "; path=/";
}

// Sahifa yuklanganda saqlangan tilni o'qib, o'rnatish
window.addEventListener('load', () => {
    // 1. Cookie'dan tilni o'qib olish (agar mavjud bo'lsa)
    const cookies = document.cookie.split(';');
    let savedLang = 'uz'; // Standart til

    cookies.forEach(cookie => {
        const parts = cookie.trim().split('=');
        if (parts[0] === 'site_lang') {
            savedLang = parts[1];
        }
    });

    // Select elementida o'sha tilni tanlab qo'yamiz
    const langSelect = document.getElementById('langSelect');
    if (langSelect) {
        langSelect.value = savedLang;
    }

    // Tilni funksiya orqali sahifaga qo'llaymiz
    switchLanguage(savedLang);

    // 2. Cookie Consent Banner Mantiqi
    if (!document.cookie.includes('cookie_accepted=true')) {
        setTimeout(() => {
            document.getElementById('cookieBanner').classList.add('active');
        }, 1000);
    }
});

function acceptCookies() {
    document.cookie = "cookie_accepted=true; max-age=" + (60 * 60 * 24 * 30) + "; path=/";
    document.getElementById('cookieBanner').classList.remove('active');
}
