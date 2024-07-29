import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';
import 'package:fta/screen/status/currentFlight/components/box1.dart';
import 'package:fta/screen/status/currentFlight/components/box2.dart';

class CurrentFlightStatus extends StatelessWidget {
  const CurrentFlightStatus({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        backgroundColor: const Color(0xffD3F5D5),
        appBar: AppBar(
          backgroundColor: const Color(0xffD3F5D5),
          title: const Text(
            'Flight Status',
            style: TextStyle(
                fontSize: 26,
                fontFamily: 'MadeTommy',
                fontWeight: FontWeight.w600),
          ),
          actions: [
            IconButton(
                onPressed: () {
                  ScaffoldMessenger.of(context).showSnackBar(
                    const SnackBar(
                      content: Text('You have subscribed to this flight updates'),
                    ),
                  );
                },
                icon: const Icon(Icons.notifications_none_outlined,
                    color: Colors.black, size: 30)),
          ],
        ),
        body: const SizedBox(
          width: double.infinity,
          height: double.infinity,
          child: SafeArea(
              child: Padding(
            padding: EdgeInsets.fromLTRB(30, 30, 30, 0),
            child: SingleChildScrollView(
                physics: BouncingScrollPhysics(),
                child: Column(
                  children: [
                    Row(
                      children: [
                        Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Text('From',
                                style: TextStyle(
                                    fontSize: 12,
                                    fontFamily: 'MadeTommy',
                                    fontWeight: FontWeight.w500)),
                            SizedBox(height: 10),
                            Text('GKP',
                                style: TextStyle(
                                    fontSize: 20,
                                    fontFamily: 'MadeTommy',
                                    fontWeight: FontWeight.w600)),
                            Text('Gorakhpur',
                                style: TextStyle(
                                    fontSize: 16,
                                    fontFamily: 'MadeTommy',
                                    fontWeight: FontWeight.w500)),
                          ],
                        ),
                        Spacer(),
                        Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Text('To',
                                style: TextStyle(
                                    fontSize: 12,
                                    fontFamily: 'MadeTommy',
                                    fontWeight: FontWeight.w500)),
                            SizedBox(height: 10),
                            Text('DEL',
                                style: TextStyle(
                                    fontSize: 18,
                                    fontFamily: 'MadeTommy',
                                    fontWeight: FontWeight.w600)),
                            Text('Delhi',
                                style: TextStyle(
                                    fontSize: 14,
                                    fontFamily: 'MadeTommy',
                                    fontWeight: FontWeight.w500)),
                          ],
                        ),
                        SizedBox(width: 50),
                      ],
                    ),

                    //--------------------------------------------------------------------------------------------------
                    SizedBox(height: 20),

                    Box1(),
                    SizedBox(height: 20),

                    Box2(),

                    SizedBox(height: 50),
                  ],
                )),
          )),
        ));
  }
}
