import 'package:firebase_auth/firebase_auth.dart';

class AuthService {
  // ignore: unused_field
  final FirebaseAuth _auth = FirebaseAuth.instance;
}

//sign in anon
Future signInAnon() async {
  try {
    var _auth;
    AuthResult result = await _auth.signInAnonymoisly();
    FirebaseUser user = result.user;
    return user;
  } catch (e) {
    print(e.toString());
    return null;
  }
}
