// $( ".header" ).load( '../header.html');
// $( "#banner" ).load( '../footer.html');




/*=============== SWIPER JS GALLERY ===============*/
// let swiperCards = new Swiper(".gallery-cards", {
//   loop: true,
//   loopedSlides: 5,
//   cssMode: true,
//   effect: 'fade',
// });
  
// let swiperThumbs = new Swiper(".gallery-thumbs", {
//   loop: true,
//   loopedSlides: 5,
//   slidesPerView: 3,
//   centeredSlides: true,
//   slideToClickedSlide: true,

//   pagination: {
//     el: ".swiper-pagination",
//     type: "fraction",
//   },
//   navigation: {
//     nextEl: ".swiper-button-next",
//     prevEl: ".swiper-button-prev",
//   },
// });

// swiperThumbs.controller.control = swiperCards;

const allFilterItems = document.querySelectorAll('.filter-item');
const allFilterBtns = document.querySelectorAll('.filter-btn');

window.addEventListener('DOMContentLoaded', () => {
    allFilterBtns[0].classList.add('active-btn');
});

allFilterBtns.forEach((btn) => {
    btn.addEventListener('click', () => {
        showFilteredContent(btn);
    });
});

function showFilteredContent(btn){
    allFilterItems.forEach((item) => {
        if(item.classList.contains(btn.id)){
            resetActiveBtn();
            btn.classList.add('active-btn');
            item.style.display = "block";
        } else {
            item.style.display = "none";
        }
    });
}

