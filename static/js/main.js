$(function () {
    //按钮状态
    $(document).on('click', '.buttons-row .button', function () {
        $(this).siblings().removeClass('active');
        $(this).addClass('active');
    });
    //解析答案
    $(document).on('click', '.resolve', function (e) {
        $(this).parents('.list-block').next('.card').removeClass('hidden');
    });
    //选择题提交答案
    $(document).on('click', '#btnchksmt', function (e) {
        var rbnitems = $(':radio').length;
        var chkitems = $(':checkbox').length;
        alert('singlechoices:' + rbnitems + '\ncheckboxchs:' + chkitems);
    });

    $.init();    //默认必须要执行$.init(),实际业务里一般不会在HTML文档里执行，通常是在业务页面代码的最后执行
    $(".swiper-container").swiper({
        speed: 600,
        spaceBetween: 100,
        autoHeight: true,
        autoplay: 5000
    })
});