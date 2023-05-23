import * as THREE from 'https://unpkg.com/three@0.138.0/build/three.module.js';
import { GLTFLoader } from 'https://unpkg.com/three@0.138.0/examples/jsm/loaders/GLTFLoader.js';

var pyramid;

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 0.1, 1000 );


// Sun (Directional Light)
var sunLight = new THREE.DirectionalLight(0xffffff, 1);
sunLight.position.set(1, 0, 1);  // The direction from which light is coming, you can change it based on your requirement
scene.add(sunLight);

const renderer = new THREE.WebGLRenderer();
renderer.setSize( window.innerWidth, window.innerHeight );
document.body.appendChild( renderer.domElement );

const loader = new GLTFLoader();
loader.load('/static/models/pyramid.glb', function (gltf) {
    pyramid = gltf.scene;
    scene.add(gltf.scene);
}, undefined, function (error) {
    console.error(error);
});


camera.position.z = 5;

function animate() {
	requestAnimationFrame( animate );
    pyramid.rotation.y += 0.01;

	renderer.render( scene, camera );

}
animate();
