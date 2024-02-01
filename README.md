if one wishes to add custom javascript to perform the actions, one can add a file to the static folder, and add the block to the html script to add the javascript as follows:-
<script
  type="text/javascript"
  src=""{{ url_for('static', filename='index.js')}}
>
