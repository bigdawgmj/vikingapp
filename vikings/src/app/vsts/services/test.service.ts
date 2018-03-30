import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/observable/of';

import { Teammate } from '../model/teammate';
import { Weather } from '../model/weather';
import { Project } from '../model/project';

@Injectable()
export class TestService {
  private baseUrl = 'api/team';

  constructor(private http: HttpClient) { }

  getTeam(): Observable<Teammate[]> {
    return this.http.get<Teammate[]>(this.baseUrl);
  }

  addMember(mate: Teammate): Observable<any> {
    return this.http.post<any>(this.baseUrl + '/member', mate);
  }

  addTraining(sprint: Object): Observable<any> {
    return this.http.post<any>('api/wit/training', sprint);
  }

  getProjects(): Observable<Project[]> {
    return this.http.get<Project[]>('api/projects');
  }

  getWeather(city: string): Observable<Weather> {
    return this.http.get<Weather>('api/weather/' + city)
  }

}
