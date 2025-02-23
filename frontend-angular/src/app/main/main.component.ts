//main.componets.ts

import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink, RouterOutlet, Router } from '@angular/router';

@Component({
  selector: 'app-main',
  standalone: true,
  imports: [CommonModule, RouterLink, RouterOutlet],
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent { 
  usuarioInfo = "Usuario"; // Simulación de información del usuario

  constructor(private router: Router) {}

  cerrarSesion() {
    console.warn("🚨 Se ejecutó cerrarSesion() automáticamente.");
    debugger;
    console.log("🚨 Se ejecutó cerrarSesion() automáticamente.");
    console.trace(); // 👀 Esto imprimirá en consola quién llamó a cerrarSesion()
    console.log("Sesión cerrada");
    localStorage.removeItem('token'); // ✅ Eliminar el token
    this.router.navigate(['/login']); // ✅ Redirigir a login
  }
}
