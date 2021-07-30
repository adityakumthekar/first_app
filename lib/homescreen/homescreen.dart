// Copyright 2020 The Flutter team. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.
import 'package:flutter/material.dart';
import 'package:store/homescreen/components/cards.dart';

class HomeScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        backgroundColor: Colors.white,
        body: ListView(
          children: [
            Cardst(
              pname: "WHEAT",
              price: "30",
            ),
            Cardst(
              pname: "RICE",
              price: "30",
            ),
            Cardst(
              pname: "RICE",
              price: "30",
            )
          ],
        ));
  }
}
