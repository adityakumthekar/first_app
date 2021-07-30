import 'package:flutter/material.dart';
import 'package:store/constant.dart';

class OrDivider extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    Size size = MediaQuery.of(context).size;
    return Container(
      width: size.width * 0.8,
      child: Row(
        children: <Widget>[
          Builddivider(),
          Padding(
            padding: const EdgeInsets.symmetric(horizontal: 10),
            child: Text(
              "OR",
              style: TextStyle(color: PrimaryDark, fontWeight: FontWeight.w600),
            ),
          ),
          Builddivider(),
        ],
      ),
    );
  }

  // ignore: non_constant_identifier_names
  Expanded Builddivider() {
    return Expanded(
      child: Divider(color: Colors.black),
    );
  }
}
