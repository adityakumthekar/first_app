import 'package:flutter/material.dart';
import 'package:flutter_svg/flutter_svg.dart';
import 'package:store/homescreen/homescreen.dart';
import 'package:store/login/bakground.dart';
import 'package:store/login/roundedinputfield.dart';
import 'package:store/rounded_button.dart';

import 'roundedpass.dart';

class Loginbody extends StatelessWidget {
  const Loginbody({
    Key key,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    Size size = MediaQuery.of(context).size;
    return Background(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: <Widget>[
          Text(
            "LOGIN",
            style: TextStyle(fontWeight: FontWeight.bold),
          ),
          SvgPicture.asset("assets/image/farmer.svg",
              height: size.height * 0.35),
          RoundedinputField(
            hintText: "Your Email",
            onChanged: (value) {},
          ),
          Roundedpass(
            onChanged: (value) {},
          ),
          RoundedButton(
            text: "LOGIN",
            press: () {
              Navigator.push(
                context,
                MaterialPageRoute(
                  builder: (context) {
                    return HomeScreen();
                  },
                ),
              );
            },
          )
        ],
      ),
    );
  }
}
