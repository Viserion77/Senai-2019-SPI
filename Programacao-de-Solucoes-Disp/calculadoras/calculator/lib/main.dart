import 'package:flutter/material.dart';
import './theme_changer.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return ThemeBuilder(
      defaultBrightness: Brightness.dark,
      builder: (context, _brightness) {
        return MaterialApp(
          title: 'Flutter Demo',
          theme: ThemeData(primarySwatch: Colors.blue, brightness: _brightness),
          home: Home(),
        );
      },
    );
  }
}

class Home extends StatefulWidget {
  @override
  _HomeState createState() => _HomeState();
}

class _HomeState extends State<Home> {
  GlobalKey<FormState> _formKey = GlobalKey<FormState>();

  TextEditingController _weightController = TextEditingController();
  TextEditingController _heightController = TextEditingController();
  String _result;
  Icon _icon;

  @override
  void initState() {
    super.initState();
    resetFields();
  }

  void resetFields() {
    _weightController.text = '';
    _heightController.text = '';
    setState(() {
      _result = 'Informe seus dados';
    });
  }

  void _changeTheme() {
    ThemeBuilder.of(context).changeTheme();
  }

  bool isSwitched = true;
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: buildAppBar(),
        body: SingleChildScrollView(
            padding: EdgeInsets.all(20.0), child: buildForm()));
  }

  AppBar buildAppBar() {
    return AppBar(
      title: Text('Calculadora de IMC'),
      actions: <Widget>[
        Switch(
          value: isSwitched,
          onChanged: (value) {
            setState(() {
              isSwitched = value;
            });
            _changeTheme();
          },
        ),
        IconButton(
          icon: Icon(Icons.refresh),
          onPressed: () {
            resetFields();
          },
        )
      ],
    );
  }

  Form buildForm() {
    return Form(
      key: _formKey,
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: <Widget>[
          buildTextFormField(
              label: "Peso (kg)",
              error: "Insira seu peso!",
              controller: _weightController),
          buildTextFormField(
              label: "Altura (cm)",
              error: "Insira uma altura!",
              controller: _heightController),
          buildTextResult(),
          buildCalculateButton(),
        ],
      ),
    );
  }

  void calculateImc() {
    double weight = double.parse(_weightController.text);
    double height = double.parse(_heightController.text) / 100.0;
    double imc = weight / (height * height);

    setState(() {
      _result = "IMC = ${imc.toStringAsPrecision(2)}\n";
      if (imc < 18.6)
        _result += "Abaixo do peso";
      else if (imc < 25.0)
        _result += "Peso ideal";
      else if (imc < 30.0)
        _result += "Levemente acima do peso";
      else if (imc < 35.0)
        _result += "Obesidade Grau I";
      else if (imc < 40.0)
        _result += "Obesidade Grau II";
      else
        _result += "Obesidade Grau IIII";
      _icon = Icon(Icons.face);
      if (imc < 18.6)
        _icon = Icon(Icons.sentiment_very_dissatisfied);
      else if (imc < 25.0)
        _icon = Icon(Icons.tag_faces);
      else if (imc < 30.0)
        _icon = Icon(Icons.insert_emoticon);
      else if (imc < 35.0)
        _icon = Icon(Icons.format_color_reset);
      else if (imc < 40.0)
        _icon = Icon(Icons.fiber_manual_record);
      else
        _icon = Icon(Icons.fiber_smart_record);
    });
  }

  Widget buildCalculateButton() {
    return Padding(
      padding: EdgeInsets.symmetric(vertical: 36.0),
      child: RaisedButton(
        onPressed: () {
          if (_formKey.currentState.validate()) {
            calculateImc();
          }
        },
        child: Text('CALCULAR', style: TextStyle(color: Colors.white)),
      ),
    );
  }

  Widget buildTextResult() {
    return Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: <Widget>[
          Padding(
            padding: EdgeInsets.symmetric(vertical: 36.0),
            child: Text(
              _result,
              textAlign: TextAlign.center,
            ),
          ),
          IconButton(
            icon: _icon,
          )
        ]);
  }

  Widget buildTextFormField(
      {TextEditingController controller, String error, String label}) {
    return TextFormField(
      keyboardType: TextInputType.number,
      decoration: InputDecoration(labelText: label),
      controller: controller,
      validator: (text) {
        return text.isEmpty ? error : null;
      },
    );
  }
}
