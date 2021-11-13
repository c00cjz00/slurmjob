<?php if (isset($_GET["img"])){ $img=trim($_GET["img"]); }else{ $img="02322379.nii"; } ?>
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width,initial-scale=1.0">
    <title>basic multiplanar</title>
    <style>
      section {
        margin: 20px;
      }
    </style>
  </head>
  <body style="font-family: sans-serif;">
    <noscript>
      <strong>niivue doesn't work properly without JavaScript enabled. Please enable it to continue.</strong>
    </noscript>

    <section>
      <h1>
        Basic multiplanar
      </h1>
      <p>
        The most basic usage of NiiVue is to display a single image in the canvas. 
      </p>
      <p>
        <h3>Controls</h3>
        <ul>
          <li>move the crosshairs: left mouse click and drag (or click around)</li>
          <li>slice scrolling: mouse or touch pad scroll up and down (pinch zoom for mobile)</li>
          <li>change intensity range: right mouse click and drag a region (mobile not supported)</li>
          <li>reset intensity: left mouse click double click (mobile not supported)</li>
        </ul>
      </p>
    </section>

    <!-- demo 1 -->
    <section>
      <div id="demo1" style="width:90%; height:400px;">
        <canvas id="gl1" height=480 width=640>
        </canvas>
      </div>
    </section>

    <section>
      <p>available color maps:</p>
      <p id="colormaps"></p>
    </section>

    <script src="niivue.js">
    </script>
    <script>
     var volumeList1 = [
       // first item is brackground image
         {
           url: "<?=$img;?>",//"./images/RAS.nii.gz", "./images/spm152.nii.gz",
           volume: {hdr: null, img: null},
           name: "mni152",
           intensityMin: 0, // not used yet
           intensityMax: 100, // not used yet
           intensityRange:[0, 100], // not used yet
           colorMap: "gray",
           opacity: 1,
           visible: true,
         },
        ] 
      var nv1 = new niivue.Niivue()
      nv1.attachTo('gl1')
      nv1.loadVolumes(volumeList1)
      nv1.setSliceType(nv1.sliceTypeMultiplanar)
      document.getElementById('colormaps').innerText = nv1.colorMaps()

    </script>
  </body>
</html>
