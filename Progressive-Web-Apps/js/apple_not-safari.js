$(function(){
  //ページ内のaタグ群を取得。aTagsに配列として代入。
   var aTags = $('a');
      //全てのaタグについて処理
  aTags.each(function(){
         //aタグのhref属性からリンク先url取得
   var url = $(this).attr('href');
  //念のため、href属性は削除
    if (url === undefined) {
      return 0;
    }else{
   $(this).removeAttr('href');
         //クリックイベントをバインド
   $(this).click(function(){
     location.href = url;

     /* マチクエ部分
     $("#fade").fadeIn(600);
     $("#loader").fadeIn(600);
     console.log(url);
     setTimeout(function(){ location.href = url; }, 800); // URLにリンクする
     */
     return false;
   });
    }
   });
  });
