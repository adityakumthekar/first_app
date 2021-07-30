import 'package:flutter/material.dart';
import 'package:store/background.dart';
import 'package:flutter_svg/svg.dart';
import 'package:store/constant.dart';
import 'package:store/login/login_screen.dart';
import 'package:store/rounded_button.dart';
import 'package:store/signup/signup.dart';

class Body extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    Size size = MediaQuery.of(context).size;
    return Background(
      child: SingleChildScrollView(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text(
              "Welcome to Kissan Store",
              style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
            ),
            SvgPicture.asset(
              "assets/image/farmer1.svg",
              height: size.height * 0.45,
            ),
            RoundedButton(
              text: "LOGIN",
              press: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (context) {
                      return LoginScreen();
                    },
                  ),
                );
              },
            ),
            RoundedButton(
              text: "Sign Up",
              color: PrimaryGrey,
              textColor: Colors.black,
              press: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (context) {
                      return SignUpScreen();
                    },
                  ),
                );
              },
            ),
          ],
        ),
      ),
    );
  }
}
