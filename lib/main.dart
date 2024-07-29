import 'package:flutter/material.dart';
import 'package:fta/screen/home/home.dart';
import 'package:fta/screen/splashScreen.dart';
import 'package:fta/screen/tab_bar.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flight Status Tracker',
      home: TabPage(),
    );
  }
}
