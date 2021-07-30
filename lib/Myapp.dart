import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

import 'body.dart';
import 'constant.dart';

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Store',
      theme: ThemeData(
          primaryColor: PrimaryDark, scaffoldBackgroundColor: Colors.white),
      home: Body(),
    );
  }
}
