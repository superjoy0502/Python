<html>
 <head>
  <title>PHP 테스트</title>
 </head>
 <body>
 <?php $('#button').on('click', function() {
  $.get('hello.php', {url : 'url' });
}); ?>
 </body>
</html>