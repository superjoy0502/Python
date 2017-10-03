<html>
 <head>
  <title>PHP 테스트</title>
 </head>
 <body>
 <?php echo htmlspecialchars($_POST['name']); ?>씨 안녕하세요.
당신은 <?php echo (int)$_POST['age']; ?>세입니다.; 
 </body>
</html>