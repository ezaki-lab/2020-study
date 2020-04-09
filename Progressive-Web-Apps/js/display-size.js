// iPad Air 2の画面比率に調整済み
/*比率拡大表示計算*/
$(window).on('touchmove.noScroll', function(e) {
    e.preventDefault();
});
$(document).ready(function () {
  display_size();
});
$(window).resize(function () {
  display_size();
});

var main_height;
var main_width;

function display_size(){

  //整数の最小値
  h_size = 187;//縦の比率
  w_size = 256;//横の比率


  window.scrollTo(0,0);
  hsize = $(window).height();
  wsize = $(window).width();
  //window_show.innerHTML ='wh'+hsize+'ww'+wsize;
  if(hsize%h_size==0 && wsize%w_size==0){
    $('.main').css('height', 100+'%');
    $('.main').css('width', 100+'%');
    $('.main').css('margin', 0);
    main_width = wsize;
    main_height = hsize;
    //window_show.innerHTML='good:'+'　wh'+hsize+'　ww'+wsize;
  }else{
    if(hsize/h_size>wsize/w_size){
      wsize_w = wsize/w_size;
      height_t = h_size*wsize_w;
      $('.main').css('height', height_t+'px');
      $('.main').css('width', 100+'%');
      $('.main').css('margin', "auto 0");
      main_width = wsize;
      main_height = height_t;
      //window_show.innerHTML='h&gt;w:'+'　wh'+hsize+'　h'+height_t+'　ww'+wsize;
    }
    else if(hsize/h_size<wsize/w_size){
      hsize_w = hsize/h_size;
      width_t = w_size*hsize_w;
      $('.main').css('height', 100+'%');
      $('.main').css('width', width_t+'px');
      $('.main').css('margin', "0 auto");
      main_width = width_t;
      main_height = hsize;
      //window_show.innerHTML='h&lt;w:'+'　wh'+hsize+'　ww'+wsize+'　w'+width_t;
    }
  }
  //font_size();
}
