import 'package:flutter/material.dart';
import 'package:store/constant.dart';
import 'package:store/login/textfieldcontainer.dart';

class RoundedinputField extends StatelessWidget {
  final String hintText;
  final IconData icon;
  final ValueChanged<String> onChanged;
  const RoundedinputField({
    Key key,
    this.hintText,
    this.icon = Icons.person,
    this.onChanged,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return TextfieldContainer(
      child: TextField(
        onChanged: onChanged,
        decoration: InputDecoration(
            icon: Icon(
              icon,
              color: PrimaryDark,
            ),
            hintText: hintText,
            border: InputBorder.none),
      ),
    );
  }
}
