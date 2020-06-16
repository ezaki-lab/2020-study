import 'package:flutter/material.dart';

main() {
  runApp(MaterialApp(
    home: Page1(),
  ));
}

class Page1 extends StatelessWidget {

  // Page2に遷移
  void goToPage2(BuildContext context) {
    Navigator.push(
      context,
      MaterialPageRoute(builder: (context) => Page2()),
    );
  }
  
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Page 1'),
      ),
      body: Center(
        child: RaisedButton(
          child: Text('Go to page 2'),
          onPressed: () => goToPage2(context),
        ),
      ),
    );
  }
}

class Page2 extends StatelessWidget {

  // Page1に戻る
  void backToPage1(BuildContext context) {
    Navigator.pop(context);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Page 2'),
      ),
      body: Center(
        child: RaisedButton(
          child: Text('Back to Page 1'),
          onPressed: () => backToPage1(context),
        ),
      ),
    );
  }
}
