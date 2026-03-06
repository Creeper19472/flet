import 'package:material_symbols_icons/symbols.dart';

List<IconData> symbolsIcons = [
  {% for name, code in icons -%}
  Symbols.{{ name }},
  {% endfor -%}
];
