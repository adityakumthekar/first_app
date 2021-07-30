import 'package:flutter/material.dart';
import 'package:store/login/loginbody.dart';

class LoginScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      body: SingleChildScrollView(child: Loginbody()),
    );
  }
}
