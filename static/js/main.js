$(function () {

    $.init();    //默认必须要执行$.init(),实际业务里一般不会在HTML文档里执行，通常是在业务页面代码的最后执行
    $(".swiper-container").swiper({
        speed: 600,
        spaceBetween: 100,
        autoHeight: true,
        autoplay: 5000
    })
});