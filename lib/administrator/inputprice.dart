import 'package:flutter/material.dart';
import 'package:store/constant.dart';
import 'package:store/login/textfieldcontainer.dart';

class InputPrice extends StatelessWidget {
  final String hintText;
  final IconData icon;
  final ValueChanged<String> onChanged;
  const InputPrice({
    Key key,
    this.icon = Icons.attach_money,
    this.onChanged,
    this.hintText,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return TextfieldContainer(
      child: TextField(
        keyboardType: TextInputType.number,
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
