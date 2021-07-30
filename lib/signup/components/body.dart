import 'package:flutter/material.dart';
import 'package:store/administrator/admin.dart';
import 'package:store/constant.dart';
import 'package:store/login/roundedinputfield.dart';
import 'package:store/login/roundedpass.dart';
import 'package:store/rounded_button.dart';
import 'package:store/signup/components/background.dart';
import 'package:store/signup/components/oedivider.dart';
import 'package:store/signup/components/socialicon.dart';

class Body extends StatelessWidget {
  final Widget child;

  const Body({Key key, @required this.child}) : super(key: key);
  @override
  Widget build(BuildContext context) {
    Size size = MediaQuery.of(context).size;
    return Background(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: <Widget>[
          Text(
            "SIGN UP",
            style: TextStyle(fontWeight: FontWeight.bold),
          ),
          // SvgPicture.asset(
          //   "assets/image/farmer.svg",
          //   height: size.height * 0.35,
          // ),
          RoundedinputField(
            hintText: "Your Email",
            onChanged: (value) {},
          ),
          Roundedpass(
            onChanged: (value) {},
          ),
          RoundedButton(
            text: "SIGN UP",
            color: PrimaryDark,
            press: () {
              Navigator.push(
                context,
                MaterialPageRoute(
                  builder: (context) {
                    return HomeScreenadmin();
                  },
                ),
              );
            },
          ),
          SizedBox(
            height: size.height * 0.03,
          ),
          OrDivider(),

          Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              Socialicon(
                iconSrc: "assets/icon/facebook.svg",
                press: () {},
              ),
              Socialicon(
                iconSrc: "assets/icon/google-plus.svg",
                press: () {},
              ),
              Socialicon(
                iconSrc: "assets/icon/twitter.svg",
                press: () {},
              ),
            ],
          )
        ],
      ),
    );
  }
}
