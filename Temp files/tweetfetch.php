<?php
require_once 'twitteroauth\src\twitteroauth.php';

define('CONSUMER_KEY', '76NyujZAbenxlmzrPidy3luRs');
define('CONSUMER_SECRET', 'OKttshVQ8DQlcuXuVvJat0IRfo4q6Ati5fxzkJaVOT64uJjMvE');
define('ACCESS_TOKEN', '807155853577043968-hkVyPM2QCeRyfbyZYJrXySIuXeHDUH1');
define('ACCESS_TOKEN_SECRET', 'hrcBWIzDHTUIrjeljK4bTOEJKzf8dpbOVGCsOmzVe7NGG');
echo "Finally";



$toa = new TwitterOAuth(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET);
if( isset($_POST["json"]) ) {
     $data = json_decode($_POST["json"]);
     $data->hashtag = ($data->hashtag);
 
    json_encode($data);


$max_id = "";
foreach (range(1, 10) as $i) { // up to 10 result pages

  $query = array(
    "q" => $data->hashtag, // Change here
    "count" => 10,
    "result_type" => "recent",
    "max_id" => $max_id,
  );
 
  $results = $toa->get('search/tweets', $query);
  
if (is_array($results) || is_object($results))
{
  foreach ($results->statuses as $result)
  {
    //echo " [" . $result->created_at . "] " . $result->user->screen_name . ": " . $result->text . PHP_EOL;
    echo $result->text." %%%%%% ";
    //echo "<br>";
    $max_id = $result->id_str; // Set max_id for the next search result page
  }
}
}
}