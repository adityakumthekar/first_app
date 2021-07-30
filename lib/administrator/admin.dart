// Copyright 2020 The Flutter team. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

import 'package:flutter/material.dart';
import 'package:store/administrator/cardsadmin.dart';

// ignore: camel_case_types
class HomeScreenadmin extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        backgroundColor: Colors.white,
        body: ListView(
          children: [
            Cardsa(
              pname: "WHEAT",
              price: "",
            ),
            Cardsa(
              pname: "RICE",
              price: "",
            ),
            Cardsa(
              pname: "RICE",
              price: "",
            )
          ],
        ));
  }
}
