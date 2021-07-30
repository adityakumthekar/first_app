import 'package:flutter/material.dart';

class Cardst extends StatelessWidget {
  final String pname;
  final String price;

  const Cardst({Key key, this.pname, this.price}) : super(key: key);

  @override
  Widget build(BuildContext context) {
// ignore: non_constant_identifier_names

    return Card(
      margin: EdgeInsets.fromLTRB(16.0, 80.0, 16.00, 0.0),
      clipBehavior: Clip.antiAlias,
      child: Column(
        children: <Widget>[
          ListTile(
            leading: Icon(Icons.arrow_drop_down_circle),
            title: Text(pname),
            subtitle: Text(
              price + 'Price/Kg/Lit',
              style: TextStyle(color: Colors.black.withOpacity(0.6)),
            ),
          ),
          // Padding(
          //   padding: const EdgeInsets.all(16.0),
          //   child: Text(
          //     'Price/Kg/Lit.',
          //     style: TextStyle(color: Colors.black.withOpacity(0.6)),
          //   ),
          // ),
          // ButtonBar(
          //   alignment: MainAxisAlignment.start,
          //   children: [
          //     FlatButton(
          //       textColor: const Color(0xFF6200EE),
          //       onPressed: () {
          //         // Perform some action
          //       },
          //       child: const Text('ACTION 1'),
          //     ),
          //     FlatButton(
          //       textColor: const Color(0xFF6200EE),
          //       onPressed: () {
          //         // Perform some action
          //       },
          //       child: const Text('ACTION 2'),
          //     ),
          //   ],
          // ),
          Image.asset(
            'assets/image/' + pname + '.png',
            width: 200,
            height: 150,
          ),
        ],
      ),
    );
  }
}
